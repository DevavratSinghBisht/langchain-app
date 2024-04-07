from config import FAISS_INDEX_PATH, HUGGINGFACE_MODELNAME, HUGGINGFACE_MODEL_KWARGS

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain import HuggingFaceHub

from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings()
faiss_doc_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
retriever = faiss_doc_store.as_retriever()

qa_template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

qa_prompt = ChatPromptTemplate.from_template(qa_template)

setup_and_qa_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)

model = HuggingFaceHub(
    repo_id=HUGGINGFACE_MODELNAME,
    model_kwargs=HUGGINGFACE_MODEL_KWARGS)
output_parser = StrOutputParser()

qa_chain = setup_and_qa_retrieval | qa_prompt | model | output_parser


chat_template ="""{human_text}"""
chat_prompt = ChatPromptTemplate.from_template(chat_template)
setup_and_qa_promt = RunnableParallel(
    {"human_text": RunnablePassthrough()}
)

chat_chain = setup_and_qa_promt | chat_prompt | model | output_parser


async def get_answer(query: str) -> str:

    print("#################### Inferencing Query ####################")
    print(f"query received : {query}")
    
    response = qa_chain.invoke(query)

    return response

async def get_model_text(human_text: str) -> str:

    print("#################### Inferencing Chat ####################")
    print(f"query received : {human_text}")
    
    response = chat_chain.invoke(human_text)

    return response