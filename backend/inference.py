from ml_config import *

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings()
db = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

llm = HuggingFaceHub(
    repo_id=HUGGINGFACE_MODELNAME,
    model_kwargs=HUGGINGFACE_MODEL_KWARGS)

chain = load_qa_chain(llm, chain_type=LANGCHAIN_QNA_CHAIN_TYPE)


async def get_answer(query: str) -> str:

    print("#################### Inferencing ####################")
    print(f"query received : {query}")
        
    docs = db.similarity_search(query)
    response = chain.invoke({"input_documents":docs, "question":query})

    return response['output_text']