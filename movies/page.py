import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        st.write("Lista de filmes:")

        AgGrid(data=movies_df, reload_data=True, key="movies_grid")
    else:
        st.warning("Nenhum filme encontrado.")
