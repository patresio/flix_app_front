import streamlit as st

from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(username=username, password=password)
    if response.get("error"):
        st.error("Falha ao realizar login: " + response.get("error"))
    else:
        st.session_state.token = response.get("access")


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
