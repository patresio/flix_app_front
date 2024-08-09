import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    if reviews:
        reviews_df = pd.json_normalize(reviews)
        st.write("Lista de avaliações:")

        AgGrid(data=reviews_df, reload_data=True, key="reviews_grid")
    else:
        st.warning("Nenhuma avaliação encontrada.")

    st.divider()

    st.title("Cadastrar nova avaliação")
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie["title"]: movie["id"] for movie in movies}

    selected_movie_title = st.selectbox("Filme", list(movie_titles.keys()))

    stars = st.slider("Estrelas", 0, 5, 0)
    comment = st.text_area("Comentario")

    if st.button("Cadastrar"):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title], stars=stars, comment=comment
        )
        if new_review:
            st.rerun()
        else:
            st.error("Erro ao cadastrar avaliação.")
