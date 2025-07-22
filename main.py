
import streamlit as st

st.set_page_config(page_title="Portail d'analyse de données", layout="centered")

st.title("📊 Portail de projets Streamlit - Formation Analyse de données")

st.markdown("Bienvenue dans la plateforme de démonstration de projets Streamlit pour débutants. Veuillez sélectionner un projet à lancer localement :")

option = st.selectbox("📁 Sélectionner un projet :", [
    "Projet 1 : Analyse des ventes - Boutique Tech",
    "Projet 2 : Satisfaction client",
    "Projet 3 : Fréquentation site web",
    "Projet 4 : Analyse des ventes - Télécommunication",
    "Projet 5 : Tableau de bord RH",
    "Projet 6 : Magasin de motos et accessoires"
])

if option == "Projet 1 : Analyse des ventes - Boutique Tech":
    st.markdown("🎯 Lancer le fichier : `app_ventes.py`")
elif option == "Projet 2 : Satisfaction client":
    st.markdown("🎯 Lancer le fichier : `app_satisfaction.py`")
elif option == "Projet 3 : Fréquentation site web":
    st.markdown("🎯 Lancer le fichier : `app_web.py`")
elif option == "Projet 4 : Analyse des ventes - Télécommunication":
    st.markdown("🎯 Lancer le fichier : `app_telecom.py`")
elif option == "Projet 5 : Tableau de bord RH":
    st.markdown("🎯 Lancer le fichier : `app_rh.py`")
elif option == "Projet 6 : Magasin de motos et accessoires":
    st.markdown("🎯 Lancer le fichier : `app_moto.py`")

st.warning("💡 Tous les fichiers de données (.xlsx) doivent être dans le même dossier que les scripts pour fonctionner correctement.")


# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)