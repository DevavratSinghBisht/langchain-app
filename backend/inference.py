from core.chain import *


async def get_answer(query: str) -> str:

    print("#################### Inferencing ####################")
    print(f"query received : {query}")
        
    docs = db.similarity_search(query)
    response = chain.invoke({"input_documents":docs, "question":query})

    return response['output_text']