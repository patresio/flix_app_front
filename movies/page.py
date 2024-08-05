import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {"id": 1, "name": "Tom Cruise", "birthday": "1962-07-03"},
    {"id": 2, "name": "Denzel Washington", "birthday": "1954-12-28"},
    {"id": 3, "name": "Denzel Washington", "birthday": "1954-12-28"},
]


def show_movies():
    st.write("Lista de filmes:")

    AgGrid(data=pd.DataFrame(movies), reload_data=True, key="movies_grid")
