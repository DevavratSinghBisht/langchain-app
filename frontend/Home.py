import streamlit as st

st.set_page_config(
    page_title="Explore Langchain",
    page_icon="🏠",
)

st.write("# Welcome to My Langchain Exploration Repo! 👋")

st.sidebar.success("Select a sample application above.")

st.markdown(
    """
    ---
    # Applications

    ## Chat Application

    ## Search Engine Application


    ---
    # Tech Stack
    ## FastAPI (Backend)



    ## Streamlit (Frontend)
    Streamlit has been used to create the frontend of the appliation.
    It is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a sample appliation from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into their [documentation](https://docs.streamlit.io)
    - Ask a question in their [community
        forums](https://discuss.streamlit.io)


    ## Docker (Deploymet)
"""
)