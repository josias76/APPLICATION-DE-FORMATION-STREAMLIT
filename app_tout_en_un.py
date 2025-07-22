
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Plateforme complète Streamlit", layout="wide")

st.title("📊 Plateforme d’analyse de données - 6 Projets intégrés")

option = st.selectbox("📁 Sélectionnez un projet :", [
    "Projet 1 : Ventes - Boutique Tech",
    "Projet 2 : Satisfaction Client",
    "Projet 3 : Fréquentation site web",
    "Projet 4 : Télécommunication",
    "Projet 5 : Tableau de bord RH",
    "Projet 6 : Ventes Motos & Accessoires"
])

if option == "Projet 1 : Ventes - Boutique Tech":
    st.header("🛒 Analyse des ventes - Boutique Tech")
    df = pd.read_excel("ventes_boutique.xlsx")
    mois = st.selectbox("Choisir le mois", df['Mois'].unique())
    produit = st.multiselect("Choisir le(s) produit(s)", df['Produit'].unique(), default=df['Produit'].unique())
    filtered = df[(df['Mois'] == mois) & (df['Produit'].isin(produit))]
    st.write(filtered)
    fig = px.bar(filtered, x="Produit", y="Chiffre_affaires", title="Chiffre d'affaires par produit")
    st.plotly_chart(fig)

elif option == "Projet 2 : Satisfaction Client":
    st.header("😊 Analyse de Satisfaction Client")
    df = pd.read_excel("satisfaction_clients.xlsx")
    st.dataframe(df.head())
    fig1 = px.histogram(df, x="Satisfaction_Service", nbins=5, title="Score de satisfaction")
    st.plotly_chart(fig1)
    fig2 = px.pie(df, names='Recommande_Service', title="Recommandation du service")
    st.plotly_chart(fig2)
    st.write("Analyse croisée (Sexe vs Satisfaction) :")
    st.dataframe(pd.crosstab(df['Sexe'], df['Satisfaction_Service']))

elif option == "Projet 3 : Fréquentation site web":
    st.header("🌐 Fréquentation du site web")
    df = pd.read_excel("frequentation_site.xlsx")
    fig1 = px.line(df, x="Date", y="Visiteurs", title="Visiteurs par jour")
    st.plotly_chart(fig1)
    fig2 = px.line(df, x="Date", y="Pages_vues", title="Pages vues", color_discrete_sequence=["green"])
    st.plotly_chart(fig2)
    fig3 = px.line(df, x="Date", y="Temps_moyen_par_visite", title="Temps moyen par visite")
    st.plotly_chart(fig3)

elif option == "Projet 4 : Télécommunication":
    st.header("📡 Ventes - Secteur Télécom")
    df = pd.read_excel("ventes_telecom.xlsx")
    mois = st.selectbox("Choisir un mois", df['Mois'].unique())
    produit = st.multiselect("Choisir le(s) service(s)", df['Produit'].unique(), default=df['Produit'].unique())
    filtered = df[(df['Mois'] == mois) & (df['Produit'].isin(produit))]
    st.write(filtered)
    fig = px.bar(filtered, x="Produit", y="Chiffre_affaires", title="Chiffre d'affaires par service")
    st.plotly_chart(fig)

elif option == "Projet 5 : Tableau de bord RH":
    st.header("🧑‍💼 Tableau de bord RH")
    df = pd.read_excel("dashboard_rh.xlsx")
    fig1 = px.pie(df, names='Département', title="Répartition par département")
    st.plotly_chart(fig1)
    fig2 = px.histogram(df, x='Âge', title='Distribution des âges')
    st.plotly_chart(fig2)
    salaires = df.groupby('Département')['Salaire'].mean().reset_index()
    fig3 = px.bar(salaires, x='Département', y='Salaire', title='Salaire moyen par département')
    st.plotly_chart(fig3)
    fig4 = px.pie(df, names='Statut', title="Statuts des employés")
    st.plotly_chart(fig4)

elif option == "Projet 6 : Ventes Motos & Accessoires":
    st.header("🏍️ Magasin de motos et accessoires")
    df = pd.read_excel("ventes_moto_accessoires.xlsx")
    produit = st.selectbox("Choisir un produit", df['Produit'].unique())
    filtered = df[df['Produit'] == produit]
    st.write(filtered)
    fig = px.line(filtered, x='Date', y='Chiffre_affaires', title=f"Chiffre d'affaires - {produit}")
    st.plotly_chart(fig)
    fig2 = px.bar(filtered, x='Date', y='Quantité_vendue', title=f"Quantité vendue - {produit}")
    st.plotly_chart(fig2)


# ---------- Bandeau de bas de page ----------
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)