from core.config import *

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings()
db = FAISS.load_local("core/faiss_index", embeddings, allow_dangerous_deserialization=True)

llm = HuggingFaceHub(
    repo_id=HUGGINGFACE_MODELNAME,
    model_kwargs=HUGGINGFACE_MODEL_KWARGS)

chain = load_qa_chain(llm, chain_type=LANGCHAIN_QNA_CHAIN_TYPE)


