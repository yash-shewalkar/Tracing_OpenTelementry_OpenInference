"use client";

import React, { useState } from "react";
import { Message, ToolCall } from "../types";
import { User, Bot, ChevronDown, ChevronRight, Check, Loader2 } from "lucide-react";

const ToolStep = ({ tool }: { tool: ToolCall }) => {
  const [expanded, setExpanded] = useState(false);
  const isPending = tool.status === "pending";

  return (
    <div className="mt-2 border border-gray-700 rounded-lg bg-gray-800/50 overflow-hidden shadow-sm">
      <button
        onClick={() => setExpanded(!expanded)}
        className="w-full flex items-center justify-between p-3 hover:bg-gray-800 transition-colors"
      >
        <div className="flex items-center gap-3">
          {isPending ? (
            <Loader2 size={16} className="text-blue-400 animate-spin" />
          ) : (
            <Check size={16} className="text-green-400" />
          )}
          <span className="font-mono text-sm text-gray-300 font-medium">
            {tool.name}
          </span>
        </div>
        {expanded ? (
          <ChevronDown size={16} className="text-gray-500" />
        ) : (
          <ChevronRight size={16} className="text-gray-500" />
        )}
      </button>

      {expanded && (
        <div className="p-3 border-t border-gray-700 bg-gray-900 text-xs font-mono text-gray-400 overflow-x-auto">
          <div className="mb-3">
            <span className="font-bold text-gray-500 uppercase tracking-wider text-[10px]">
              Input
            </span>
            <pre className="mt-1 bg-gray-800 p-2 rounded border border-gray-700">
              {JSON.stringify(tool.args, null, 2)}
            </pre>
          </div>
          {tool.result && (
            <div>
              <span className="font-bold text-gray-500 uppercase tracking-wider text-[10px]">
                Output
              </span>
              <pre className="mt-1 bg-gray-800 p-2 rounded border border-gray-700 whitespace-pre-wrap">
                {tool.result}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export const ChatMessage = ({ message }: { message: Message }) => {
  const isUser = message.role === "human";

  return (
    <div className="flex gap-4 w-full py-6 px-2 hover:bg-gray-800/30 transition-colors group rounded-xl">
      <div className="shrink-0 mt-1">
        {isUser ? (
          <div className="w-8 h-8 rounded-md bg-orange-500/20 flex items-center justify-center text-orange-400 shadow-sm">
            <User size={18} />
          </div>
        ) : (
          <div className="w-8 h-8 rounded-md bg-blue-600 flex items-center justify-center text-white shadow-sm">
            <Bot size={18} />
          </div>
        )}
      </div>

      <div className="flex-1 min-w-0">
        <div className="font-semibold text-sm text-gray-200 mb-2">
          {isUser ? "You" : "Agent"}
        </div>

        {!isUser && message.toolCalls && message.toolCalls.length > 0 && (
          <div className="mb-4 flex flex-col gap-2">
            {message.toolCalls.map((tool) => (
              <ToolStep key={tool.id} tool={tool} />
            ))}
          </div>
        )}

        {message.content && (
          <div className="prose prose-sm prose-invert max-w-none text-gray-300 leading-relaxed whitespace-pre-wrap">
            {message.content}
          </div>
        )}
      </div>
    </div>
  );
};