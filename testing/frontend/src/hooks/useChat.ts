// frontend/src/hooks/useChat.ts
import { useState, useCallback } from "react";
import { v4 as uuidv4 } from "uuid";
import { Message, ToolCall } from "../types";

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = useCallback(async (content: string) => {
    const userMessage: Message = { id: uuidv4(), role: "human", content };
    const aiMessageId = uuidv4();
    
    setMessages((prev) => [
      ...prev,
      userMessage,
      { id: aiMessageId, role: "ai", content: "", toolCalls: [] }
    ]);
    
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: content }),
      });

      if (!response.body) throw new Error("No response body");

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let done = false;

      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;
        if (value) {
          const chunk = decoder.decode(value, { stream: true });
          const lines = chunk.split("\n\n");
          
          for (const line of lines) {
            if (line.startsWith("data: ")) {
              const data = JSON.parse(line.replace("data: ", ""));
              
              setMessages((prev) => prev.map((msg) => {
                if (msg.id !== aiMessageId) return msg;

                if (data.type === "token") {
                  return { ...msg, content: msg.content + data.content };
                } 
                
                if (data.type === "tool_start") {
                  const newToolCall: ToolCall = {
                    id: data.id,
                    name: data.name,
                    args: data.input || {},
                    status: "pending",
                  };
                  return { ...msg, toolCalls: [...(msg.toolCalls || []), newToolCall] };
                } 
                
                if (data.type === "tool_end") {
                  const updatedToolCalls = (msg.toolCalls || []).map((tc) =>
                    tc.id === data.id
                      ? { ...tc, status: "completed" as const, result: JSON.stringify(data.output) }
                      : tc
                  );
                  return { ...msg, toolCalls: updatedToolCalls };
                }

                return msg;
              }));
            }
          }
        }
      }
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setIsLoading(false);
    }
  }, []);

  return { messages, isLoading, sendMessage };
}