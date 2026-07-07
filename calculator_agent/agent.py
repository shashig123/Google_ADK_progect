# Travel Agent

# Calculator Agent

# Weather Agent

# DevOps Agent
# calculator project
from google.adk.agents import Agent


def add(a: float, b: float):
    return a + b


def subtract(a: float, b: float):
    return a - b


def multiply(a: float, b: float):
    return a * b


def divide(a: float, b: float):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


root_agent = Agent(
    name="calculator_agent",
    model="gemini-2.5-flash",
    description="A simple calculator agent",
    instruction="""
You are a calculator assistant.

Whenever the user asks for mathematical operations,
use the appropriate tool.

Never calculate manually if a tool is available.
""",
    tools=[
        add,
        subtract,
        multiply,
        divide
    ]
)