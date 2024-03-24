import inference
from pydantic import BaseModel
from fastapi import FastAPI

class ChatModel(BaseModel):
    query: str

app = FastAPI()

@app.post('/chat')
async def chat(query: ChatModel) -> dict[str, str]:
    answer = await inference.get_answer(query.query)
    return {'response': answer}