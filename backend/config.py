################ ML CONFGS ################ 
FAISS_INDEX_PATH = "document_store/faiss_index"

HUGGINGFACE_MODELNAME = "google/flan-t5-base"
HUGGINGFACE_MODEL_KWARGS = {"temperature":0, "max_length":512}

################ WEB CNFIGS ################ 
ALLOW_ORIGINS = ['http://localhost:8501',]
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]