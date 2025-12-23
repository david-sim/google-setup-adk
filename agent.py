"""
Google ADK Agent - Main agent logic and entry point.

This is a basic agent setup following the Google ADK documentation at:
https://google.github.io/adk-docs/get-started/python/#installation
"""

from google.adk.agents import LlmAgent


def get_current_time(city: str) -> dict:
    """
    Returns the current time in a specified city.
    
    This is an example tool function that demonstrates how to add
    custom tools to your agent.
    
    Args:
        city: The name of the city to get the time for
        
    Returns:
        A dictionary with the status, city name, and time information
    """
    # This is a mock implementation. In a real scenario, you would
    # integrate with a time API or library
    return {
        "status": "success",
        "city": city,
        "message": f"This is a sample tool. Please implement actual time lookup for {city}."
    }


# Define the root agent
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='root_agent',
    description="A helpful assistant that can provide information and answer questions.",
    instruction=(
        "You are a helpful assistant powered by Google's Gemini model. "
        "You can answer questions, provide information, and help users with various tasks. "
        "Use the available tools when appropriate to provide accurate and helpful responses."
    ),
    tools=[get_current_time],
)
