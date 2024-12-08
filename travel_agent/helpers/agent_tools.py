from langchain_community.utilities.google_serper import GoogleSerperAPIWrapper
from langchain.tools import tool
import os


@tool()
def google_search(query: str) -> str:
    """Use this tool to answer questions about current events, news, or the current state of the world where up-to-date information is required."""
    serper = GoogleSerperAPIWrapper(serper_api_key=os.getenv("SERPER_API_KEY"))
    return serper.run(query)


@tool()
def finalize_plan():
    """
    This function only be used when user ask for the final plan for the user's travel plan otherwise do not use it. Each event or location in the plan
    is detailed with the following properties: place name, location, and a short description.

    When the user is satisfied with the proposed plan and wants to finalize it, this tool formats and returns
    the information in a structured way, making it easy to display or process further.

    The output will include a list of events or locations formatted as follows:

    - place_name: Name of the location or activity.
    - location: The geographical location of the place or activity.
    - description: A brief description of the place or activity.

    Example output:
    {
        "place_name": "Gardens by the Bay",
        "location": "18 Marina Gardens Dr, Singapore 018953",
        "description": "A futuristic park with stunning plant exhibits, including the iconic Supertree Grove and Cloud Forest."
    }
    """
    return {
        "parameters": {
            "type": "object",
            "properties": {
                "place_name": {
                    "type": "string",
                    "description": "The name of the location or activity (e.g., 'Gardens by the Bay'). This is the primary identifier of the event or place.",
                },
                "location": {
                    "type": "string",
                    "description": "The geographical location of the activity or event (e.g., 'Marina Bay, Singapore'). Helps the user understand where the event takes place.",
                },
                "description": {
                    "type": "string",
                    "description": "A brief summary of what the event or location is about (e.g., 'A stunning botanical garden with iconic structures like the Supertree Grove'). This gives the user context about the event or place.",
                },
            },
            "required": [
                "place_name",
                "location",
                "description",
            ],
        },
    }
