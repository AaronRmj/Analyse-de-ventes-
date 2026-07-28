import streamlit as st
from utils.auth import login, register

st.header("Application analyse de ventes")

if "user" not in st.session_state:
    st.session_state["user"] = None

choix = st.sidebar.selectbox(
    label="Choisissez une action",
    options=["Connexion", "Créer un compte", "Déconnexion"]
)

if choix == "Connexion":
    with st.form("authentification"):
        st.subheader("Connectez-vous")
        email = st.text_input("Email")
        password = st.text_input("Mot de passe", type="password")
        submit = st.form_submit_button("Se connecter")
        if submit:
            user = login(email, password)

            if user:
                st.session_state["user"] = user
                st.success("Vous êtes connecté")
                
            else:
                st.error("Mot de passe ou email incorrect")

elif choix == "Créer un compte":
    st.subheader("Creation de compte")
    with st.form("register"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        password = st.text_input("Mot de passe", type="password")
        confirmation = st.text_input("Confirmer le mot de passe")
        submit = st.form_submit_button("Creer votre compte")

        if submit:
            if confirmation != password:
                st.error("Les mots de passe ne se correspondent pas")
            else:    
                register(nom, email, password)
                st.success("Compte créé avec succès")
                

elif choix == "Déconnexion":
    st.session_state["user"] = None
    st.success("Déconnecté")
    st.rerun()