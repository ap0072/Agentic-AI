from app.langchain_agent import run_agent

async def handle_teams_message(body):
    user_input = body.get("text", "")
    response = run_agent(user_input)
    return response

