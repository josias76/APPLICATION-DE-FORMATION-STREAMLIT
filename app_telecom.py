
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analyse des ventes - Secteur Télécommunication")
st.markdown("Scénario : Vous êtes analyste chez un opérateur télécom. Votre mission est de suivre les ventes mensuelles de services.")

df = pd.read_excel("ventes_telecom.xlsx")

mois = st.selectbox("Choisir un mois", df['Mois'].unique())
produit = st.multiselect("Choisir le(s) service(s)", df['Produit'].unique(), default=df['Produit'].unique())

filtered = df[(df['Mois'] == mois) & (df['Produit'].isin(produit))]

st.write("### Données filtrées", filtered)

fig = px.bar(filtered, x="Produit", y="Chiffre_affaires", title="Chiffre d'affaires par produit")
st.plotly_chart(fig)


# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)