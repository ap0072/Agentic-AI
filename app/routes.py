from fastapi import APIRouter, Request
from app.teams_handler import handle_teams_message

router = APIRouter()

@router.post("/api/messages")
async def messages(request: Request):
    body = await request.json()
    response = await handle_teams_message(body)
    return {"response": response}

