from agno.agent import Agent
from agno.tools.x import XTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIResponses 
from dotenv import load_dotenv
import os 

db = SqliteDb("memory.db")

load_dotenv()  # Load environment variables from .env file
os.environ.setdefault("OPENAI_API_KEY", os.getenv("api_key"))
def build_agent():
    agent = Agent(
        db=db,
        name="Memory Agent",
        model=OpenAIResponses(id="gpt-5.2", api_key=os.getenv("api_key")),
        markdown=True, # to get the formated ouput
        add_history_to_context=True,
    )
    return agent
agent = build_agent()

agent.print_response("capital of pakistan")
agent.print_response("best time to vist it")