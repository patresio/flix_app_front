import plotly.express as px
import streamlit as st

from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movies_stats()

    st.title("Estatisticas de Filmes e Genêros")

    if len(movie_stats["movies_by_genre"]) > 0:
        st.subheader("Total de filmes por genêro: ")
        fig = px.pie(
            movie_stats["movies_by_genre"],
            values="count",
            names="genre__name",
            title="Filmes por genêro",
        )
        st.plotly_chart(fig)

    st.subheader("Quantidade de filmes por generos: ")
    for genre in movie_stats["movies_by_genre"]:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader("Total de filmes cadastrados: ")
    st.write(movie_stats["total_movies"])

    st.subheader("Total de avaliaçoes cadastradas: ")
    st.write(movie_stats["total_reviews"])

    st.subheader("Média Geral de Estrelas nas Avaliações: ")
    st.write(movie_stats["average_stars"])
