import streamlit as st
import requests
import json

from config import BACKED_URL

with st.sidebar:
    st.title('Chatbot')

# Write a message if none exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Clear all messages
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Take and display user prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Function for calling backend
def get_response(prompt_input):
    response = requests.post(BACKED_URL,
                             json = {"query": prompt_input})
    response = json.loads(response.content.decode())
    print(response)
    return response['response']

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(prompt)
        st.write(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)