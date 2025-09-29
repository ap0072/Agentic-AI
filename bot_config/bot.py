from botbuilder.core import ActivityHandler, TurnContext
from app.langchain_agent import run_agent

class TeamsBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        response = run_agent(user_input)
        await turn_context.send_activity(response)

