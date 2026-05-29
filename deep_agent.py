# import os
# from typing import Literal

# from tavily import TavilyClient
# from deepagents import create_deep_agent
# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv
# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

# tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


# from typing import Literal

# def internet_search(
#     query: str,
#     max_results: int = 5,
#     topic: Literal["general", "news", "finance"] = "general",
#     include_raw_content: bool = False,
# ):
#     """
#     Search the internet for current information.

#     Use this tool whenever external information is required.
#     """

#     print(f"\n[TOOL EXECUTED]")
#     print(f"query={query}")
#     print(f"max_results={max_results}")
#     print(f"topic={topic}")

#     return {
#         "query": query,
#         "results": [
#             {
#                 "title": "India launches new AI initiative",
#                 "content": "The Indian government announced a major AI initiative focused on research, innovation and digital infrastructure."
#             },
#             {
#                 "title": "Monsoon progresses across India",
#                 "content": "Weather agencies reported further monsoon advancement with rainfall expected in several states."
#             },
#             {
#                 "title": "Indian stock market gains",
#                 "content": "Benchmark indices closed higher amid positive investor sentiment and strong earnings expectations."
#             }
#         ]
#     }
    
# # System prompt to steer the agent to be an expert researcher
# research_instructions = """You are an expert context managed under 7k tokens agent.

# You have access to an internet search tool as your primary means of gathering information.

# ## `internet_search`

# Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included. Keep Max results to at max 3 and you are allowed to call the tool only at max twice.
# You should keep your context as small and short as possible.

# """

# model = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0,
#     verbose=True,
#     max_tokens=1500,
#     streaming=True,
# )



# agent = create_deep_agent(
#     model=model,
#     tools=[internet_search],
#     system_prompt=research_instructions,
    
# )


# inputs = {
#     "messages": [
#         {
#             "role": "user",
#             "content": "Tell top 3 news in India and give 50 words breif on each, I want quick answer"
#         }
#     ]
# }

# stream = agent.stream_events(
#     inputs,
#     version="v3"
# )

# # coordinator messages
# for message in stream.messages:
#     print("\n[AGENT]", flush=True)

#     for delta in message.text:
#         print(delta, end="", flush=True)

# # coordinator tool calls
# for call in stream.tool_calls:
#     print("\n[TOOL CALL]")
#     print("NAME:", call.tool_name)
#     print("INPUT:", call.input)

#     for delta in call.output_deltas:
#         print(delta, end="", flush=True)

#     if call.completed:
#         print("\nOUTPUT:")
#         print(call.output)

# # subagents
# for subagent in stream.subagents:
#     print(f"\n[SUBAGENT] {subagent.name}")

#     for message in subagent.messages:
#         for delta in message.text:
#             print(delta, end="", flush=True)

#     for call in subagent.tool_calls:
#         print("\nSUB TOOL:", call.tool_name)
#         print("INPUT:", call.input)

        
# # for message in stream.messages:
# #     print(message.text, end="", flush=True)

# # result = agent.invoke({"messages": [{"role": "user", "content": "give latest news in India! top news only,  I want quick answekr"}]})

# # # Print the agent's response
# # print(result["messages"][-1].content)


# # llm = ChatGroq(
# #     model="openai/gpt-oss-120b",
# #     streaming=True,
# # )

# # for chunk in llm.stream("Write a 500 word essay on AI"):
# #     print(chunk.content, end="", flush=True)


# import os
# from typing import Literal
# from tracing import setup_tracing

# setup_tracing(
#     project_name="deep-agent-project",
#     service_name="deep-agent"
# )
# from dotenv import load_dotenv
# from deepagents import create_deep_agent
# from langchain_groq import ChatGroq

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# def internet_search(
#     query: str,
#     max_results: int = 5,
#     topic: Literal["general", "news", "finance"] = "general",
#     include_raw_content: bool = False,
# ):
#     """
#     Fake internet search tool.

#     Use when external information is required.
#     """

#     return {
#         "query": query,
#         "results": [
#             {
#                 "title": "India launches AI Mission",
#                 "content": "Government expands national AI initiatives."
#             },
#             {
#                 "title": "Monsoon advances",
#                 "content": "Weather department reports monsoon progress."
#             },
#             {
#                 "title": "Stock market rises",
#                 "content": "Major indices closed higher today."
#             }
#         ]
#     }


# research_instructions = """
# You are an expert context-managed agent.

# Rules:
# - Keep context under 7000 tokens.
# - Use tools only when needed.
# - Maximum 2 tool calls.
# - Keep answers concise.
# """

# model = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0,
#     streaming=True,
#     max_tokens=1500,
# )

# agent = create_deep_agent(
#     model=model,
#     tools=[internet_search],
#     system_prompt=research_instructions,
# )


# def get_agent():
#     return agent



import os
import json
import math
import random
import asyncio

from datetime import datetime
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

# =====================================================
# TOOLS
# =====================================================

@tool
def get_weather(city: str) -> str:
    """Get weather information."""

    data = {
        "city": city,
        "temperature": 32,
        "condition": "Sunny",
        "humidity": 48
    }

    return json.dumps(data, indent=2)


@tool
def currency_converter(
    amount: float,
    from_currency: str,
    to_currency: str
) -> str:
    """Convert currency."""

    rates = {
        "USD": 83.0,
        "INR": 1.0,
        "EUR": 91.0
    }

    inr_value = amount * rates[from_currency]
    converted = inr_value / rates[to_currency]

    return f"{amount} {from_currency} = {round(converted, 2)} {to_currency}"


@tool
def calculator(expression: str) -> str:
    """Evaluate mathematical expression."""

    allowed = {
        "__builtins__": {},
        "sqrt": math.sqrt,
        "pow": pow
    }

    result = eval(expression, allowed)

    return str(result)


@tool
def stock_price(symbol: str) -> str:
    """Get stock price."""

    prices = {
        "AAPL": 212.45,
        "MSFT": 468.22,
        "NVDA": 1104.21
    }

    price = prices.get(symbol.upper(), 0)

    change = round(random.uniform(-5, 5), 2)

    return f"{symbol.upper()} price is ${price} ({change}%)"


@tool
def current_time(city: str) -> str:
    """Get current time."""

    return f"{city} time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


# =====================================================
# MODEL
# =====================================================

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    streaming=True,
    max_tokens=1500,
)

# =====================================================
# STATE
# =====================================================

class AgentState(TypedDict):

    query: str

    tasks: List[Dict[str, Any]]

    tool_results: Dict[str, Any]

    final_response: str


# =====================================================
# NODES
# =====================================================

def planner_node(state: AgentState):

    planner_prompt = f"""
    Extract independent tool calls.

    Available tools:
    - get_weather(city)
    - currency_converter(amount, from_currency, to_currency)
    - calculator(expression)
    - stock_price(symbol)
    - current_time(city)

    Return ONLY JSON list.

    Query:
    {state['query']}
    """

    response = llm.invoke(planner_prompt)

    tasks = json.loads(response.content)

    return {
        "tasks": tasks
    }


async def executor_node(state: AgentState):

    tool_map = {
        "get_weather": get_weather,
        "currency_converter": currency_converter,
        "calculator": calculator,
        "stock_price": stock_price,
        "current_time": current_time,
    }

    async def run_tool(task):

        tool_name = task["tool"]

        args = task["args"]

        result = await asyncio.to_thread(
            tool_map[tool_name].invoke,
            args
        )

        return tool_name, result

    results = await asyncio.gather(
        *[run_tool(t) for t in state["tasks"]]
    )

    return {
        "tool_results": dict(results)
    }


def synthesizer_node(state: AgentState):

    synthesis_prompt = f"""
    User Query:
    {state['query']}

    Tool Results:
    {json.dumps(state['tool_results'], indent=2)}

    Answer naturally.
    """

    response = llm.invoke(synthesis_prompt)

    return {
        "final_response": response.content
    }


# =====================================================
# GRAPH
# =====================================================

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("executor", executor_node)
builder.add_node("synthesizer", synthesizer_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "executor")
builder.add_edge("executor", "synthesizer")
builder.add_edge("synthesizer", END)

graph = builder.compile()


# =====================================================
# PUBLIC API FOR CHAINLIT
# =====================================================

# backend.py

async def stream_agent(query: str):
    # Using version="v3" for typed projections
    stream = await graph.astream_events({"query": query}, version="v3")
    
    # Yield tokens as they arrive
    async for message in stream.messages:
        if message.text:
            yield {"type": "token", "content": message.text}
    
    # Yield final result
    yield {"type": "final", "content": stream.output}