from datetime import datetime

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService
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

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor["name"]: actor["id"] for actor in actors}
    selected_actor_name = st.multiselect("Atores", list(actor_names.keys()))

    selected_actors_id = [actor_names[actor] for actor in selected_actor_name]

    resume = st.text_area("Resumo do filme")

    if st.button("Cadastrar"):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_id,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error("Falha ao criar filme. Verifique os dados e tente novamente.")
