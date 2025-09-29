from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool
from app.aws_tools import invalidate_cloudfront
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

cloudfront_tool = Tool(
    name="CloudFrontInvalidator",
    func=lambda input: invalidate_cloudfront(distribution_id=input),
    description="Use this tool to invalidate CloudFront cache. Input should be a distribution ID."
)

agent = initialize_agent(
    tools=[cloudfront_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def run_agent(prompt):
    return agent.run(prompt)

