
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("frequentation_site.xlsx")

st.title("Suivi de la fréquentation du site web")

fig1 = px.line(df, x="Date", y="Visiteurs", title="Évolution du nombre de visiteurs")
st.plotly_chart(fig1)

fig2 = px.line(df, x="Date", y="Pages_vues", title="Pages vues par jour", color_discrete_sequence=["green"])
st.plotly_chart(fig2)

fig3 = px.line(df, x="Date", y="Temps_moyen_par_visite", title="Temps moyen passé par visite (minutes)")
st.plotly_chart(fig3)
