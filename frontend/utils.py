import streamlit as st
import requests
import json

def create_sidebar(title: str, desrciption:str) -> None:
    '''
        Creates the sidebar in the UI.

        param:
            title       (str)   : title of the sidebar
            description (str)   : description of the page

        return: None
    '''

    with st.sidebar:
        st.title(title)
        st.write(desrciption)

class Request:

    def __init__(self) -> None:
        pass

    @staticmethod
    def post(url, payload) -> dict:
        '''
            Functon making post call to backend.

            param:
                url     (str)   : url to send request to
                payload (str)   : payload to be sent to the url
        '''

        try:
            response = requests.post(url, json = payload)
            response = json.loads(response.content.decode())

        except:
            # st.error("An error occurred while calling backend.")
            print(f"An error occurred while calling backend. Endpoint : {url}")
            return {'answer': 'Error while calling backend.', }
        
        return response