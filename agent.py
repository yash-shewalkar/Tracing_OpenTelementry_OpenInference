# aggent.py

import os
import json
import math
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


from tracing import setup_tracing

setup_tracing(
    project_name="create-agent-project",
    service_name="create-agent"
)

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# =========================
# TOOLS
# =========================

@tool
def get_weather(city: str) -> str:
    """Get current weather information for a city."""

    weather_data = {
        "Pune": {
            "temperature": 32,
            "condition": "Sunny",
            "humidity": 48,
            "wind_speed": 12
        },
        "Mumbai": {
            "temperature": 30,
            "condition": "Cloudy",
            "humidity": 70,
            "wind_speed": 18
        },
        "Delhi": {
            "temperature": 39,
            "condition": "Hot",
            "humidity": 25,
            "wind_speed": 9
        }
    }

    return json.dumps(
        weather_data.get(
            city,
            {
                "temperature": 28,
                "condition": "Unknown",
                "humidity": 50,
                "wind_speed": 10
            }
        ),
        indent=2
    )


@tool
def currency_converter(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert currency between INR, USD, EUR."""

    rates = {
        "USD": 83.0,
        "INR": 1.0,
        "EUR": 91.0
    }

    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency."

    inr_value = amount * rates[from_currency]
    converted = inr_value / rates[to_currency]

    return f"{amount} {from_currency} = {round(converted, 2)} {to_currency}"


@tool
def calculator(expression: str) -> str:
    """Safely evaluate mathematical expressions."""

    allowed = {
        "__builtins__": {},
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round
    }

    try:
        result = eval(expression, allowed)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"


@tool
def stock_price(symbol: str) -> str:
    """Get mock stock price."""

    prices = {
        "AAPL": 212.45,
        "MSFT": 468.22,
        "GOOGL": 178.91,
        "TSLA": 189.12,
        "NVDA": 1104.21
    }

    price = prices.get(symbol.upper())

    if not price:
        return "Stock not found."

    change = round(random.uniform(-5, 5), 2)

    return f"{symbol.upper()} current price is ${price} ({change}%)"


@tool
def current_time(city: str) -> str:
    """Get current time for a city."""

    return f"Current time in {city} is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


# =========================
# MODEL
# =========================

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    verbose=True,
    max_tokens=2000,
    reasoning_effort="high",
    streaming=True,
)


# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """

    You are a helpful assistant and answers the user's query in concise conversational way rather than a input ouptut machine and natural way with the help of tools as the base and grounded info to format/frame your answer.
Your responsibilities:
- Use tools whenever needed
- Reason step-by-step
- Combine outputs from multiple tools
- Give concise but accurate answers
- Prefer tools over assumptions


    You have to divide or use user's query to create title for your response or flow in which you want to show or give the answer. Try to be conversational and talkitive


"""


# =========================
# AGENT
# =========================

agent = create_agent(
    model=model,
    tools=[
        get_weather,
        currency_converter,
        calculator,
        stock_price,
        current_time
    ],
    system_prompt=SYSTEM_PROMPT
)


# =========================
# USER QUERY
# =========================

query = """
I am traveling to Mumbai Imagica for a trip tomorrow.

I want to know the current weather there and also as I came from US I have 500 USD which I need to convert into INR today, tell me how much will I get in INR and can I sponsor my trip with that amount.  calculate the contri for 4 people in that amount as 2  childern,  in the 4 people including me and my wife and a couple. I am paying all prices together and want to know the contri for that couple to give as I will cover expenses of myself, my wife and children.   ticket price for adults is 700rs each and for children is 500rs.
"""


# =========================
# RUN AGENT
# =========================

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
)


# =========================
# TRACE PARSER
# =========================

messages = result["messages"]

tool_calls = []
tool_outputs = []
final_response = None
total_tokens = 0

for msg in messages:

    # Tool calls
    if hasattr(msg, "tool_calls") and msg.tool_calls:

        for tc in msg.tool_calls:
            tool_calls.append(
                {
                    "tool": tc["name"],
                    "input": tc["args"]
                }
            )

    # Tool outputs
    if msg.__class__.__name__ == "ToolMessage":

        tool_outputs.append(
            {
                "tool": msg.name,
                "output": msg.content
            }
        )

    # Final response
    if (
        msg.__class__.__name__ == "AIMessage"
        and not msg.tool_calls
    ):
        final_response = msg.content

    # Tokens
    if hasattr(msg, "usage_metadata") and msg.usage_metadata:
        total_tokens += msg.usage_metadata.get("total_tokens", 0)


# =========================
# PRINT RESULTS
# =========================

print("\n==============================")
print("ENTERPRISE AGENT EXECUTION")
print("==============================\n")

print("TOOLS CALLED:\n")

for idx, tc in enumerate(tool_calls, start=1):

    print(f"{idx}. Tool Name: {tc['tool']}")
    print(f"   Input: {tc['input']}\n")


print("\nTOOL OUTPUTS:\n")

for idx, output in enumerate(tool_outputs, start=1):

    print(f"{idx}. Tool: {output['tool']}")
    print(f"   Output: {output['output']}\n")


print("\nFINAL AGENT RESPONSE:\n")
print(final_response)

print("\nTOTAL TOKENS CONSUMED:")
print(total_tokens)

print("\n==============================")