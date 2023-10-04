import streamlit as st
import joblib
# import requests

def formulaires():
    # récupération du dictionnaire de labelencoders
    values_list = joblib.load('encoders')

    # Titre de l'application
    st.title("Formulaire:")

    # Input de type number
    age = st.number_input("Saisissez l'âge", min_value=0, max_value=100, step=1)

    # Input avec plusieurs options
    job = st.selectbox("Sélectionnez l'emploi", values_list['job'].classes_.tolist())
    marital = st.selectbox("Sélectionnez l'état civil", values_list['marital'].classes_.tolist())
    education = st.selectbox("Sélectionnez le niveau d'étude", values_list['education'].classes_.tolist())

    # Champ de type case à cocher à deux choix
    default = st.checkbox("Le crédit est-il en défaut ?")

    # Input de type number
    balance = st.number_input("Saisissez votre solde", min_value=-5000, max_value=5000, step=1, value=0)

    # Champ de type case à cocher à deux choix
    housing = st.checkbox("Un prêt logement a-t-il été contracté ?")
    loan = st.checkbox('Un prêt personnel a-t-il été contracté ?')

    # Input avec plusieurs options
    contact = st.selectbox("type de communication du contact",  values_list['contact'].classes_.tolist())


    # Input de type number
    date = st.number_input("Dernier jour du contact du mois", min_value=0, max_value=31, step=1)

    # Input avec plusieurs options
    month = st.selectbox("type de communication du contact",  values_list['month'].classes_.tolist())


    # Input de type number
    duration = st.number_input("Durée du dernier contact, en secondes", min_value=0, max_value=5000, step=1)
    campaign = st.number_input('Nombre de contacts effectués pendant cette campagne', min_value=0, max_value=10, step=1)
    pdays = st.number_input("Nombre de jours écoulés après que le client a été contacté pour la dernière fois lors d'une campagne précédente", min_value=-1, step=1)
    previous = st.number_input('Nombre de contacts effectués avant cette campagne et pour ce client', min_value=0, step=1)

    # Input avec plusieurs options
    poutcome = st.selectbox('résultat de la campagne marketing précédente', values_list['poutcome'].classes_.tolist())

    # Bouton pour soumettre le formulaire
    if st.button("Soumettre"):
        st.session_state.page = "Response" 
        data_json = {"age": age, "job": job, "marital": marital, "education": education, "default": default, 
        "balance": balance, "housing": housing, "loan": loan, "contact": contact, "date": date, "month": month,
        "duration": duration, "compaign": campaign, "pdays": pdays, "previous": previous, "poutcome": poutcome}
        st.session_state.donnees_formulaire = data_json
        # st.write(data_json)
        # response = requests.post('http://127.0.0.0.0:8000/predict', json= data_json)
        # return response.json()
        

def response():
    if hasattr(st.session_state, "donnees_formulaire"):
        st.write("Données soumises:")
        st.write(st.session_state.donnees_formulaire)
    else:
        st.warning("Aucune donnée de formulaire soumise.")
    
# Vérifiez l'état actuel pour décider quelle page afficher
if "page" not in st.session_state:
    st.session_state.page = "Formulaire"

if st.session_state.page == "Formulaire":
    formulaires()
elif st.session_state.page == "Response":
    response()

print(st.session_state)




