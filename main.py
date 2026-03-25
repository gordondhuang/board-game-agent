from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent

load_dotenv()

class Response(BaseModel):
  topic: str
  summary: str
  sources: list[str]
  tools_used: list[str]



# Setup
llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic()

# Parser
parser = PydanticOutputParser(pydantic_object=Response)

# Prompt
prompt = f"""
You are an expert board game master that knows how to play games and can teach players.
Answer the user query.

Wrap the output EXACTLY in this format:
{parser.get_format_instructions()}
"""

# Agent
agent = create_agent(
  model=llm,
  tools=[]
)

output = agent.invoke({
  "messages": [
    ("system", prompt),
    ("user", "How do you play Monopoly?")
  ]
})

output_text = output["messages"][-1].content

try:
  structured_response = parser.parse(output_text)
  print(structured_response)
except Exception as e:
  print("Error parsing response", e, "Response: ", output)


