import streamlit as st

from actors.page import show_actors
from genres.page import show_genres
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if "token" not in st.session_state:
        show_login()
    else:
        st.title("Flix APP")

        menu_option = st.sidebar.selectbox(
            "Selecione uma opção",
            [
                "Inicio",
                "Genêros",
                "Filmes",
                "Atores/Atriz",
                "Avaliações",
            ],
        )

        if menu_option == "Inicio":
            st.write("Inicio")

        if menu_option == "Genêros":
            show_genres()

        if menu_option == "Filmes":
            show_movies()

        if menu_option == "Atores/Atriz":
            show_actors()

        if menu_option == "Avaliações":
            show_reviews()


if __name__ == "__main__":
    main()
