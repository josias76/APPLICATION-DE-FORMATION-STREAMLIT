
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analyse des ventes - Magasin de motos et accessoires")
st.markdown("Scénario : En tant qu’analyste, vous devez produire un tableau de bord des ventes journalières de motos et accessoires pour motards.")

df = pd.read_excel("ventes_moto_accessoires.xlsx")

produit = st.selectbox("Choisir un produit", df['Produit'].unique())
filtered = df[df['Produit'] == produit]

st.write("### Détail des ventes pour :", produit)
st.dataframe(filtered)

# Chiffre d'affaires dans le temps
fig = px.line(filtered, x='Date', y='Chiffre_affaires', title="Chiffre d'affaires quotidien pour " + produit)
st.plotly_chart(fig)

# Quantité vendue
fig2 = px.bar(filtered, x='Date', y='Quantité_vendue', title="Quantité vendue par jour")
st.plotly_chart(fig2)
