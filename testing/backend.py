import json
import os
from random import randint
from datetime import datetime
from typing import Literal

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from langchain.tools import tool
from langchain_core.messages import HumanMessage

from langchain_groq import ChatGroq

# =========================================================
# IMPORTANT IMPORTS
# =========================================================

from langchain.agents import create_agent
from deepagents import create_deep_agent
from deepagents import CompiledSubAgent

# =========================================================
# ENV
# =========================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =========================================================
# FAKE TOOLS (SUPERVISOR)
# =========================================================

@tool
def internet_search(
    query: str,
    max_results: int = 3,
    topic: Literal["general", "news", "finance"] = "general",
):
    """
    Search internet for information.
    """

    return {
        "query": query,
        "topic": topic,
        "results": [
            {
                "title": "AI breakthrough announced",
                "content": "Researchers released new AI models."
            },
            {
                "title": "Markets rise",
                "content": "Global markets closed higher."
            },
            {
                "title": "Weather update",
                "content": "Monsoon expected this week."
            }
        ]
    }


@tool
def vector_search(query: str):
    """
    Semantic vector database retrieval.
    """

    return {
        "matches": [
            "Relevant document chunk 1",
            "Relevant document chunk 2",
            "Relevant document chunk 3"
        ]
    }


@tool
def analytics_engine(metric: str):
    """
    Enterprise analytics engine.
    """

    return {
        "metric": metric,
        "value": randint(100, 10000),
        "trend": "upward"
    }

# =========================================================
# SUBAGENT TOOLS
# =========================================================

@tool
def github_actions(repo: str):
    """
    Fetch CI/CD pipeline status.
    """

    return {
        "repository": repo,
        "status": "passing",
        "last_build": datetime.now().isoformat()
    }


@tool
def database_query(sql: str):
    """
    Execute enterprise SQL query.
    """

    return {
        "rows_returned": randint(1, 25),
        "preview": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }

# =========================================================
# MODEL
# =========================================================

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    streaming=True, 
    max_tokens=2000,
)

# =========================================================
# CREATE NORMAL LANGCHAIN AGENT
# =========================================================

engineering_agent = create_agent(
    model=model,
    tools=[
        github_actions,
        database_query
    ],
    system_prompt="""
You are an Engineering Agent.

Responsibilities:
- Handle engineering tasks
- Handle SQL/database tasks
- Handle CI/CD tasks
- Be concise
"""
)

# =========================================================
# COMPILE SUBAGENT
# =========================================================

engineering_subagent = {
    "name": "engineering_agent",

    "description": """
Handles:
- engineering tasks
- CI/CD tasks
- database tasks
""",

    "system_prompt": """
You are an Engineering Agent.

Responsibilities:
- Handle engineering tasks
- Handle SQL/database tasks
- Handle CI/CD tasks
- Be concise
""",

    "agent": engineering_agent
}

# =========================================================
# SUPERVISOR DEEP AGENT
# =========================================================

supervisor_agent = create_deep_agent(
    model=model,
    tools=[
        internet_search,
        vector_search,
        analytics_engine
    ],
    subagents=[
        engineering_subagent
    ],
    system_prompt="""
You are a Supervisor Deep Agent.

Rules:
- Delegate engineering/database tasks to engineering_agent
- Use tools only when necessary
- Keep answers concise
"""
)

# =========================================================
# FASTAPI
# =========================================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# REQUEST MODEL
# =========================================================

class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default-thread"

# =========================================================
# SSE EVENT STREAM
# =========================================================

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):

    async def event_generator():

        config = {
            "configurable": {
                "thread_id": req.thread_id
            }
        }

        async for event in supervisor_agent.astream_events(
            {
                "messages": [
                    HumanMessage(content=req.message)
                ]
            },
            config=config,
            version="v2"
        ):

            event_type = event["event"]

            # =====================================================
            # CHAIN START
            # =====================================================

            if event_type == "on_chain_start":

                payload = {
                    "type": "chain_start",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # CHAIN END
            # =====================================================

            elif event_type == "on_chain_end":

                payload = {
                    "type": "chain_end",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # RETRIEVER START
            # =====================================================

            elif event_type == "on_retriever_start":

                payload = {
                    "type": "retriever_start",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                    "input": event["data"].get("input"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # RETRIEVER END
            # =====================================================

            elif event_type == "on_retriever_end":

                payload = {
                    "type": "retriever_end",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                    "output": event["data"].get("output"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # PROMPT START
            # =====================================================

            elif event_type == "on_prompt_start":

                payload = {
                    "type": "prompt_start",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # PROMPT END
            # =====================================================

            elif event_type == "on_prompt_end":

                payload = {
                    "type": "prompt_end",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # TOOL START
            # =====================================================

            elif event_type == "on_tool_start":

                payload = {
                    "type": "tool_start",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                    "input": event["data"].get("input"),
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # TOOL END
            # =====================================================

            elif event_type == "on_tool_end":

                raw_output = event["data"].get("output")

                if hasattr(raw_output, "content"):
                    safe_output = raw_output.content
                else:
                    safe_output = raw_output

                payload = {
                    "type": "tool_end",
                    "name": event.get("name"),
                    "run_id": event.get("run_id"),
                    "output": safe_output,
                }

                yield f"data: {json.dumps(payload)}\n\n"

            # =====================================================
            # TOKEN STREAM
            # =====================================================

            elif event_type == "on_chat_model_stream":

                chunk = event["data"]["chunk"]

                if chunk.content:

                    payload = {
                        "type": "token",
                        "content": chunk.content
                    }

                    yield f"data: {json.dumps(payload)}\n\n"

        # =====================================================
        # DONE
        # =====================================================

        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

# =========================================================
# RUN
# =========================================================

# uvicorn main:app --reload