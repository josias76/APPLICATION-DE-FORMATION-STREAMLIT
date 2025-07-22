
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("satisfaction_clients.xlsx")

st.title("Analyse de Satisfaction Client")

st.write("Aperçu des données :", df.head())

fig1 = px.histogram(df, x="Satisfaction_Service", nbins=5, title="Répartition des scores de satisfaction")
st.plotly_chart(fig1)

fig2 = px.pie(df, names='Recommande_Service', title="Clients qui recommandent le service")
st.plotly_chart(fig2)

st.write("Analyse croisée (Genre vs Satisfaction) :")
st.write(pd.crosstab(df['Sexe'], df['Satisfaction_Service']))


# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)