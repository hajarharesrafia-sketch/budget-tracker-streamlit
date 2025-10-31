

# --- Import des bibliothèques nécessaires ---
import streamlit as st
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

# --- Configuration générale de la page ---
st.set_page_config(page_title="Suivi de Budget", page_icon="💰", layout="wide")

# --- Titre et description ---
st.title(" Application de Suivi de Budget")
st.write("Ajoutez vos revenus et dépenses, et suivez votre solde en temps réel.")

# ==============================
# Chargement ou création du fichier CSV
# ==============================

def load_data():
    """Charge le fichier CSV contenant les transactions, ou le crée s'il n'existe pas."""
    try:
        data = pd.read_csv("data/transactions.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Date", "Catégorie", "Type", "Montant", "Description"])
        data.to_csv("data/transactions.csv", index=False)
    return data

# Chargement initial
data = load_data()

# ==============================
# Formulaire d'ajout de transaction
# ==============================

st.header("➕ Ajouter une nouvelle transaction")

with st.form("transaction_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        d = st.date_input("Date", value=date.today())  # Sélection de la date
    with col2:
        categorie = st.selectbox(
            "Catégorie",
            ["Salaire", "Alimentation", "Transport", "Loisirs", "Santé", "Autres"]
        )
    with col3:
        type_ = st.radio("Type", ["Revenu", "Dépense"])  # Choix du type

    montant = st.number_input("Montant (€)", min_value=0.0, step=0.5)
    description = st.text_input("Description (facultatif)")

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        # Création d'une nouvelle ligne
        new_row = pd.DataFrame({
            "Date": [d],
            "Catégorie": [categorie],
            "Type": [type_],
            "Montant": [montant],
            "Description": [description]
        })

        # ✅ Ajout direct à la DataFrame
        data = pd.concat([data, new_row], ignore_index=True)

        # ✅ Sauvegarde dans le CSV
        data.to_csv("data/transactions.csv", index=False)

        # ✅ Message de confirmation
        st.success("✅ Transaction ajoutée avec succès !")

        # ✅ Relance immédiate pour actualiser le tableau et le graphique
        st.rerun()

# ==============================
# Affichage du tableau complet
# ==============================

st.header("📋 Historique des transactions")
st.dataframe(data)

# ==============================
# Résumé du budget
# ==============================

st.header("📊 Résumé du budget")

# Conversion du montant en numérique
data["Montant"] = pd.to_numeric(data["Montant"], errors="coerce")

# Calculs de base
revenus = data[data["Type"].str.lower().str.strip() == "revenu"]["Montant"].sum()
depenses = data[data["Type"].str.lower().str.strip() == "dépense"]["Montant"].sum()
solde = revenus - depenses

# Affichage sous forme de métriques
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenus", f"{revenus:.2f} €", "+")
col2.metric("Total Dépenses", f"{depenses:.2f} €", "-")
col3.metric("Solde", f"{solde:.2f} €")

# ==============================
# Visualisation graphique
# ==============================

st.header("📈 Visualisation des dépenses par catégorie")

# Filtrer les dépenses uniquement
depenses_df = data[data["Type"].str.lower().str.strip() == "dépense"]

# Regrouper les dépenses par catégorie
depenses_par_categorie = (
    depenses_df.groupby("Catégorie")["Montant"]
    .sum()
    .sort_values(ascending=False)
)

# Affichage du graphique
if not depenses_par_categorie.empty:
    fig, ax = plt.subplots()
    bars = ax.bar(depenses_par_categorie.index, depenses_par_categorie.values, color="red", alpha=0.8)

    # Ajouter les montants au-dessus de chaque barre
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f"{yval:.0f}€", ha="center", va="bottom")

    ax.set_title("Dépenses par catégorie", fontsize=16, fontweight="bold")
    ax.set_xlabel("Catégorie")
    ax.set_ylabel("Montant (€)")
    plt.xticks(rotation=45)

    st.pyplot(fig)
else:
    st.info("Aucune dépense enregistrée pour le moment.")
