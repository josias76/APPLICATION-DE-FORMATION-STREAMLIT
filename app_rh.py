
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Tableau de bord RH simplifié")
st.markdown("Scénario : En tant qu'analyste RH, vous devez explorer les caractéristiques du personnel de votre entreprise.")

df = pd.read_excel("dashboard_rh.xlsx")

# Visualisation par département
fig1 = px.pie(df, names='Département', title="Répartition par département")
st.plotly_chart(fig1)

# Histogramme des âges
fig2 = px.histogram(df, x='Âge', title='Distribution des âges')
st.plotly_chart(fig2)

# Moyenne des salaires par département
salaires = df.groupby('Département')['Salaire'].mean().reset_index()
fig3 = px.bar(salaires, x='Département', y='Salaire', title='Salaire moyen par département')
st.plotly_chart(fig3)

# Statuts
fig4 = px.pie(df, names='Statut', title="Statut des employés")
st.plotly_chart(fig4)

# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)