from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=["actors", "genre.id"])
        st.write("Lista de filmes:")

        AgGrid(data=movies_df, reload_data=True, key="movies_grid")
    else:
        st.warning("Nenhum filme encontrado.")

    st.divider()
    st.title("Cadastrar novo filme")
    title = st.text_input("Titulo do filme")
    release_date = st.date_input(
        label="Data de lancamento",
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre["name"]: genre["id"] for genre in genres}
    selected_genre_name = st.selectbox("Genero", list(genre_names.keys()))
