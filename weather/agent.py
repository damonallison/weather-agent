import google.adk.agents.agent_config
from google.adk.agents.llm_agent import Agent
from zoneinfo import ZoneInfo
from datetime import datetime


def get_current_weather(city: str) -> dict[str, str]:
    """Get the current weather in a city.

    Args:
        city (str): The city to get the weather for.

    Returns:
        dict[str, str]: A dict with the weather information or an error message.
    """

    if city.lower() == "london":
        return {
            "status": "success",
            "city": city,
            "temperature": "72 degrees",
            "conditions": "sunny",
        }
    return {
        "status": "error",
        "error_message": "City not found",
    }


def get_current_time(city: str) -> dict[str, str]:
    """Get the current time in a city.

    Args:
        city (str): The city to get the time for.

    Returns:
        dict[str, str]: A dict with the time information or an error message.
    """
    if city.lower() == "london":
        now = datetime.now(ZoneInfo("Europe/London"))
        return {
            "status": "success",
            "city": city,
            "time": now.strftime("%Y-%m-%d %H:%M:%S %Z%z"),
        }
    return {
        "status": "error",
        "error_message": "City not found",
    }


root_agent = Agent(
    model="gemini-3-flash-preview",
    name="root_agent",
    # The model uses `description` to determine whether to delegate control to
    # the agent.
    description="An agent that determines the current weather and time in a given city.",
    instruction="You are a helpful agent that answers questions about the weather and time in a city.",
    tools=[get_current_weather, get_current_time],
)
