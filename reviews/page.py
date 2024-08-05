import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

reviews = [
    {"id": 1, "name": "Tom Cruise", "birthday": "1962-07-03"},
    {"id": 2, "name": "Denzel Washington", "birthday": "1954-12-28"},
    {"id": 3, "name": "Denzel Washington", "birthday": "1954-12-28"},
]


def show_reviews():
    st.write("Lista de avaliações:")

    AgGrid(data=pd.DataFrame(reviews), reload_data=True, key="reviews_grid")
