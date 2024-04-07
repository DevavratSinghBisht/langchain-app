import streamlit as st
from config import QUERY_URL
from utils import Request, create_sidebar

TITLE = "Question Answering System"
DESCRIPTION =   """
                    This appliation illustrates the use of 
                    Steamlit, FastAPI and Langchain for creating a Question Answering System.
                    Enjoy exploring the application! 
                    """

def main():
    '''
        Setup the page, create search box and show response.

        param   : None
        return  : None
    '''
    
    # setup page
    st.set_page_config(page_title="Question Answering System", page_icon="🔍")
    st.title(TITLE)
    create_sidebar(TITLE, DESCRIPTION)
    
    # create search box and show response
    if search_text := st.chat_input("Ask a question"):
        response = Request.post(QUERY_URL, {"query":search_text})
        if response != None:
            st.write(response['answer'])

if __name__ == "__main__":
    main()