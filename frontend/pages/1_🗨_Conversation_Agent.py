import streamlit as st
from config import CHAT_URL, DEFAULT_MESSAGE, CHAT_ROLE_ASSISTANT, CHAT_ROLE_USER
from utils import Request, create_sidebar

TITLE = "Conversation Agent"
DESCRIPTION =   """
                    This appliation illustrates the use of 
                    Steamlit, FastAPI and Langchain for creating a conversation agent. 
                    Enjoy exploring the application! 
                    """

def setup_page():
    """
        Sets page titile and creates sidebar.

        param: none
        return: none

    """
    st.set_page_config(page_title="Question Answering System2", page_icon="🔍")
    st.title(TITLE)
    create_sidebar(TITLE, DESCRIPTION)

def set_side_bar_button():
    """
        Sidebar button to clear all the message from current session state.

        param: None
        return: None
    """
    def clear_chat_history():
        st.session_state.messages = [DEFAULT_MESSAGE]
    st.sidebar.button('Clear History', on_click=clear_chat_history)

def write_message_if_none_exists():
    """
        Displays a default message on startup or refresh.

        param: None
        return: None
    """
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [DEFAULT_MESSAGE]

def write_all_message():
    """
        Displays all messages in the current session state.

        param: None
        return: None
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def get_and_set_response():
    """
        Takes input from user and shows it in the message container.
        Calls backed to get the agent's response and displays in the message container.

        param:
            prompt (str) : user text for which the response has to be generated

        return: None
    """

    # Get promt from user and print
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": CHAT_ROLE_USER, "content": prompt})
        with st.chat_message(CHAT_ROLE_USER):
            st.write(prompt)

    # Get agent's response from backend and print
    if st.session_state.messages[-1]["role"] != CHAT_ROLE_ASSISTANT:
        with st.chat_message(CHAT_ROLE_ASSISTANT):
            
            with st.spinner("Thinking..."):
                response = Request.post(CHAT_URL, {"query": prompt})

            st.write(response['answer'])
            message = {"role": CHAT_ROLE_ASSISTANT, "content": response['answer']}
        
        st.session_state.messages.append(message)

def main():
    """
        Method to run all other methods in sequence.

        param: none
        return: none
    """
    setup_page()
    set_side_bar_button()
    write_message_if_none_exists()
    write_all_message()
    get_and_set_response()

if __name__ == "__main__":
    main()