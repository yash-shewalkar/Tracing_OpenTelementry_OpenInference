import os
import json
import math
import random
import asyncio

from datetime import datetime
from typing import TypedDict, Dict, Any, List

from tracing import setup_tracing
setup_tracing(
    project_name="dag-agent-project",
    service_name="dag-agent"
)

from langgraph.graph import StateGraph, END

from langchain_groq import ChatGroq
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


# =====================================================
# ENV
# =====================================================


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


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
    model="openai/gpt-oss-120b",
    temperature=0,
    reasoning_effort="high",
    max_tokens=2000,
    streaming=True,
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
# PLANNER NODE
# =====================================================

def planner_node(state: AgentState):

    query = state["query"]

    planner_prompt = f"""
    You are a planning agent.

    Extract independent tool calls from the query.

    Available tools:
    - get_weather(city)
    - currency_converter(amount, from_currency, to_currency)
    - calculator(expression)
    - stock_price(symbol)
    - current_time(city)

    Return ONLY valid JSON list.
    Privide Strucutred output
    Example:
    [
      {{
        "tool": "get_weather",
        "args": {{
          "city": "Pune"
        }}
      }}
    ]

    Query:
    {query}
    """

    response = llm.invoke(planner_prompt)

    tasks = json.loads(response.content)

    return {
        "tasks": tasks
    }


# =====================================================
# PARALLEL EXECUTOR NODE
# =====================================================

async def executor_node(state: AgentState):

    tasks = state["tasks"]

    tool_map = {
        "get_weather": get_weather,
        "currency_converter": currency_converter,
        "calculator": calculator,
        "stock_price": stock_price,
        "current_time": current_time
    }

    async def run_tool(task):

        tool_name = task["tool"]

        args = task["args"]

        tool = tool_map[tool_name]

        result = await asyncio.to_thread(
            tool.invoke,
            args
        )

        return tool_name, result

    results = await asyncio.gather(
        *[run_tool(task) for task in tasks]
    )

    return {
        "tool_results": dict(results)
    }


# =====================================================
# SYNTHESIZER NODE
# =====================================================

def synthesizer_node(state: AgentState):

    query = state["query"]

    tool_results = state["tool_results"]

    synthesis_prompt = f"""
    You are a helpful assistant and answers the user's query in concise and natural way with the help of the context of tool results as the base and grounded info to format/frame your answer.
    This is the
    User Query:
    {query}

    This are the 
    Tool Results for this user query:
    {json.dumps(tool_results, indent=2)}

    You have to divide or use user's query to create title for your response or flow in which you want to show or give the answer. 

    """

    response = llm.invoke(synthesis_prompt)

    return {
        "final_response": response.content
    }


# =====================================================
# BUILD GRAPH
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
# QUERY
# =====================================================

query = """
I am traveling to Mumbai Imagica for a trip tomorrow.

I want to know the current weather there and also as I came from US I have 500 USD which I need to convert into INR today, tell me how much will I get in INR and can I sponsor my trip with that amount.  calculate the contri for 4 people in that amount as 2  childern,  in the 4 people including me and my wife and a couple. I am paying all prices together and want to know the contri for that couple to give as I will cover expenses of myself, my wife and children.   ticket price for adults is 700rs each and for children is 500rs.


"""


# =====================================================
# RUN GRAPH
# =====================================================

result = asyncio.run(

    graph.ainvoke(
        {
            "query": query
        }
    )

)


# =====================================================
# OUTPUT
# =====================================================

print("\n==============================")
print("LANGGRAPH DAG EXECUTION")
print("==============================\n")

print("TASKS:\n")

for task in result["tasks"]:

    print(task)

print("\nTOOL RESULTS:\n")

for k, v in result["tool_results"].items():

    print(f"{k}:")
    print(v)
    print()

print("\nFINAL RESPONSE:\n")

print(result["final_response"])

print("\n==============================")