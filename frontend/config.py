################ WEB CONFIGS ################ 
# BACKEND_URI = "http://172.17.0.1:8000"
LOCALHOST_URI = "http://localhost:8000"
BACKEND_URI = LOCALHOST_URI
HEALTH_URL = f"{BACKEND_URI}/"
QUERY_URL = f"{BACKEND_URI}/query"
CHAT_URL = f"{BACKEND_URI}/chat"


################ CHAT CONFIGS ################
CHAT_DEFAULT_MESSAGE_CONTENT = "How may I assist you today?"
CHAT_ROLE_ASSISTANT = "assistant"
CHAT_ROLE_USER = "user"
DEFAULT_MESSAGE = {"role": CHAT_ROLE_ASSISTANT, "content": CHAT_DEFAULT_MESSAGE_CONTENT}