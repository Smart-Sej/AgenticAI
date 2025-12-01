from datetime import datetime

from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    """
    Docstring for get_current_time
    
    :return: Time in format YYYY-MM-DD HH:MM:SS
    :rtype: dict
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assisstant that can use the following tools:
    -get_current_time
    """,
    tools=[get_current_time],
)