import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:

        st.write("Lista de Genêros:")
        genres_df = pd.json_normalize(genres)
        AgGrid(data=genres_df, reload_data=True, key="genres_grid")
    else:
        st.warning("Nenhum genêro encontrado.")

    st.divider()
    st.title("Cadastrar novo genêro")
    name = st.text_input("Nome do genêro")
    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.success(f"Genêro '{name}' criado com sucesso!")
            st.rerun()
        else:
            st.error("Falha ao criar genêro. Verifique os dados e tente novamente.")
