from google.adk.agents import Agent
from .tools import get_weather

root_agent = Agent(
    name="weather_agent",

    model="gemini-2.5-flash",

    description="Weather information agent",

    instruction="""
You are a weather assistant.

Whenever the user asks about weather,
temperature,
climate,
forecast,
or rain,

use the get_weather tool.
""",

    tools=[get_weather],
)