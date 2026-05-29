// frontend/src/types.ts
export interface ToolCall {
  id: string;
  name: string;
  args: Record<string, unknown>;
  result?: string;
  status: "pending" | "completed" | "error";
}

export interface Message {
  id: string;
  role: "human" | "ai";
  content: string;
  toolCalls?: ToolCall[];
}