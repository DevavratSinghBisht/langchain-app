import inference
from pydantic import BaseModel
from fastapi import FastAPI

class ChatModel(BaseModel):
    text: str

app = FastAPI()

@app.post('/chat')
async def chat(text: ChatModel):
    bot_respponse = await inference.get_response(text)
    return {'response': bot_respponse}