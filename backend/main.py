import inference
from data_models import QueryModel, AnswerModel, HealthModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://localhost:8501',]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def health_check() -> HealthModel:
    return HealthModel()

@app.post('/query')
async def query(query: QueryModel) -> AnswerModel:
    answer = await inference.get_answer(query.query)
    response = AnswerModel(**query.model_dump(), answer=answer)
    return response