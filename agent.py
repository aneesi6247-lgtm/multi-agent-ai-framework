from agno.agent import Agent
from agno.tools.x import XTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

from agno.models.openai import OpenAIResponses 
from dotenv import load_dotenv
import os 

load_dotenv()  # Load environment variables from .env file
os.environ.setdefault("OPENAI_API_KEY", os.getenv("api_key"))
x_tools = XTools(
    wait_on_rate_limit=True # Retry when rate limits are reached
)


def build_agent():
    agent = Agent(
        name="My Agent",
        description="Intereact with X to get the latest news about politics",
        model=OpenAIResponses(id="gpt-5.2", api_key=os.getenv("api_key")),
        markdown=True, # to get the formated ouput
        add_datetime_to_context=True,
        tools=[DuckDuckGoTools()]

    )
    return agent
agent = build_agent()
response = agent.run("what is the latest situation of iran and USA war?")
print(response.content)