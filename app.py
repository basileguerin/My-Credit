import streamlit as st
# import requests
# import pydantic

# Titre de l'application
st.title("Formulaire:")

# # Champ de texte
# age = st.text_input("Entrez votre âge")

# Input de type number
age = st.number_input("Saisissez votre âge", min_value=0, max_value=100, step=1)

# Input avec plusieurs options
job = st.selectbox("Sélectionnez une option", ["admin.", "inconnu", "chômeur", "gestion", "femme de ménage", "entrepreneur", "étudiant", "col bleu", "indépendant", "retraité", "technicien", "services"])
marital = st.selectbox('Sélectionnez une option', ["marié", "divorcé", "célibataire"])
education = st.selectbox('Sélectionnez une option', ["inconnu", "secondaire", "primaire", "tertiaire"])

# Champ de type case à cocher à deux choix
default = st.checkbox("Le crédit est-il en défaut ?")

# Input de type number
balance = st.number_input("Saisissez votre solde", min_value=-5000, max_value=5000, step=1, value=0)

# Champ de type case à cocher à deux choix
housing = st.checkbox("Avez-vous contracter un prêt logement ?")
loan = st.checkbox('Avez-vous contracter un prêt personnel ?')

# Input avec plusieurs options
contact = st.selectbox("type de communication du contact",  ["inconnu", "téléphone", "cellulaire"])

# Input de type number
date = st.number_input("Dernier jour du contact du mois", min_value=0, max_value=31, step=1)

# Input avec plusieurs options
month = st.selectbox("type de communication du contact",  ["janvier", "février", "mars", "avril", "mai", "juin", 'juillet', 'septembre', 'octobre', 'novembre', 'decembre'])

# Input de type number
duration = st.number_input("Durée du dernier contact, en secondes", min_value=0, max_value=5000, step=1)
campaign = st.number_input('Nombre de contacts effectués pendant cette campagne', min_value=0, max_value=10, step=1)
pdays = st.number_input("Nombre de jours écoulés après que le client a été contacté pour la dernière fois lors d'une campagne précédente", min_value=-1, step=1)
previous = st.number_input('Nombre de contacts effectués avant cette campagne et pour ce client', min_value=0, step=1)

# Input avec plusieurs options
poutcome = st.selectbox('résultat de la campagne marketing précédente', [ "inconnu", "autre", "échec", "succès"])

# Bouton pour soumettre le formulaire
if st.button("Soumettre"):
    st.write("Age :", age, ", job:", job, ', marital:', marital, ', education:', education, ', défaut', default, ', solde:', balance )
    st.write('logement: ', housing, ', prêt personnel:', loan, ', contact:', contact, ', date:', date, ', mois:', month)
    st.write('duration:', duration, ', compaign:', campaign, ', pdays:', pdays, ', previous:', previous, ', poutcome:', poutcome)
    # response = requests.get('http://127.0.0.0.0:8000/square?n=5')
    # st.write(response)
