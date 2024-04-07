import inference
from config import ALLOW_ORIGINS, ALLOW_CREDENTIALS, ALLOW_METHODS, ALLOW_HEADERS
from data_models import QueryModel, AnswerModel, HealthModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS
)

@app.get('/')
def health_check() -> HealthModel:
    return HealthModel()

@app.post('/query')
async def query(query: QueryModel) -> AnswerModel:
    answer = await inference.get_answer(query.query)
    response = AnswerModel(**query.model_dump(), answer=answer)
    return response

@app.post('/chat')
async def chat(human_text: QueryModel) -> AnswerModel:
    answer = await inference.get_model_text(human_text.query)
    response = AnswerModel(**human_text.model_dump(), answer=answer)
    return response