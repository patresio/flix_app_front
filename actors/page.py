import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService


def show_actors():
    actors_service = ActorService()
    st.write("Lista de Atores/Atrizes:")
    actors_df = pd.json_normalize(actors_service.get_actors())
    AgGrid(data=pd.DataFrame(actors_df), reload_data=True, key="actors_grid")

    st.divider()
    st.title("Cadastrar novo(a) ator/atriz")
    name = st.text_input("Nome do(a) ator/atriz")
    st.date_input("Data de Nascimento")
    if st.button("Cadastrar"):
        st.success(f"Ator/atriz '{name}' criado com sucesso!")
