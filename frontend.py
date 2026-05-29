import chainlit as cl

from deep_agent import run_agent


@cl.on_chat_start
async def start():

    await cl.Message(
        content="LangGraph DAG Agent Ready"
    ).send()


@cl.on_message
async def main(message: cl.Message):

    async with cl.Step(
        name="Planner",
        type="run"
    ) as planner_step:

        planner_step.output = "Generating execution plan..."

    result = await run_agent(message.content)

    async with cl.Step(
        name="Tasks",
        type="run"
    ) as step:

        step.output = str(result["tasks"])

    async with cl.Step(
        name="Tool Results",
        type="tool"
    ) as step:

        step.output = str(result["tool_results"])

    await cl.Message(
        content=result["final_response"]
    ).send()