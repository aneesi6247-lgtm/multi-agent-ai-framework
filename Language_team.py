from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

from agno.models.openai import OpenAIResponses 
from dotenv import load_dotenv
import os 

load_dotenv()  # Load environment variables from .env file
os.environ.setdefault("OPENAI_API_KEY", os.getenv("api_key"))

eng_agent = Agent(name= "English Agent", description = "You translate the input into english")
german_agent = Agent(name= "German Agent", description = "You translate the input into German")
Urdu_agent = Agent(name= "Urdu Agent", description = "You translate the input into Urdu")

team = Team(
    name = "Language Team",
    members = [eng_agent, german_agent, Urdu_agent],
    description = """ You are a team of three agents, each agent is responsible for translating the input into a specific language. Print the repsonse of each agent""",
    tools = [DuckDuckGoTools()]
)
response = team.run("Main ty maira maira dil barjani")
print(response.content)