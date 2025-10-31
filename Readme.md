<!-- 💰 SUIVI DE BUDGET – APPLICATION WEB STREAMLIT -->

# 💰 Suivi de Budget – Application Web Streamlit

<!-- 🎯 OBJECTIF DU PROJET -->
## 🎯 Objectif du projet
Cette application a été développée dans le cadre du projet **Python : Développement d'une WebApp interactive avec Streamlit**.  
Elle permet à l’utilisateur de **suivre ses revenus et ses dépenses** de manière simple et intuitive, avec une **visualisation graphique** du budget.

---

<!-- 🧠 FONCTIONNALITÉS PRINCIPALES -->
## 🧠 Fonctionnalités principales

- **Ajout de transactions** (revenus ou dépenses) via un formulaire interactif.  
- **Enregistrement automatique** des données dans un fichier CSV (`transactions.csv`).  
- **Calcul du total des revenus, dépenses et solde actuel**.  
- **Visualisation graphique** des dépenses par catégorie.  
- **Mise à jour en temps réel** après chaque ajout de transaction.

---

<!-- 🖥️ APERÇU DE L’INTERFACE -->
## 🖥️ Aperçu de l’interface

L’application affiche :
1. Un formulaire d’ajout de transaction :
   - Date  
   - Catégorie (Alimentation, Transport, Santé…)  
   - Type (Revenu ou Dépense)  
   - Montant et description  
2. Un tableau récapitulatif des transactions enregistrées.  
3. Des **indicateurs clés** : total des revenus, total des dépenses, et solde.  
4. Un **graphique** des dépenses par catégorie (barres rouges).  

---

<!-- ⚙️ TECHNOLOGIES UTILISÉES -->
## ⚙️ Technologies utilisées

- **Python 3.11**  
- **Streamlit** – pour l’interface web interactive  
- **Pandas** – pour la gestion et l’analyse des données  
- **Matplotlib** – pour la visualisation des dépenses  

---

<!-- 🚀 INSTALLATION ET EXÉCUTION -->
## 🚀 Installation et exécution

### 🧩 Étapes d’installation
```bash
# 1️⃣ Cloner le dépôt
git clone https://github.com/hajarharesrafia-sketch/budget-tracker-streamlit.git
cd budget-tracker-streamlit

# 2️⃣ Créer un environnement virtuel (facultatif)
conda create -n budget_env python=3.11
conda activate budget_env

# 3️⃣ Installer les dépendances
pip install streamlit pandas matplotlib

# 4️⃣ Lancer l’application
streamlit run app.py
