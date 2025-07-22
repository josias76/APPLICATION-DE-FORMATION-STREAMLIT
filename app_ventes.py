
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("ventes_boutique.xlsx")

st.title("Tableau de bord des ventes - TechStore")

mois = st.selectbox("Choisir le mois", df['Mois'].unique())
produit = st.multiselect("Choisir le(s) produit(s)", df['Produit'].unique(), default=df['Produit'].unique())

filtered = df[(df['Mois'] == mois) & (df['Produit'].isin(produit))]

st.write("Données filtrées :", filtered)

fig = px.bar(filtered, x="Produit", y="Chiffre_affaires", title="Chiffre d'affaires par produit")
st.plotly_chart(fig)
