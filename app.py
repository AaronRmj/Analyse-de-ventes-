import streamlit as st
from utils.auth import login, register

#titre principale
st.header("Application analyse de ventes")

choix = st.sidebar.selectbox(
    label="Choisissez une action",
    options= ["Connexion", "Créer un compte", "Déconnexion"]
)



if choix == "Connexion":
    st.subheader("Connectez-vous")
    st.text_input("Email")
    st.text_input("Mot de passe", type="password")