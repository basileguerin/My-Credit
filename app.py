import streamlit as st
import joblib
from functions import *  

# récupération du dictionnaire de encoders
values_list = joblib.load('encoders')

# dictionnaire des valeurs min/max ou options
values = {
        'age': {
            'min': 18,
            'max': 95
        },
        'job': values_list['job'].classes_.tolist(),
        'marital': values_list['marital'].classes_.tolist(),
        'education': values_list['education'].classes_.tolist(),

        'balance': {
            'min': -8019,
            'max': 1021270
        },
        'contact': values_list['contact'].classes_.tolist(),
        'day': {
            'min': 1,
            'max': 31
        },
        'month': values_list['month'].classes_.tolist(),
        'duration': {
            'min': 0,
            'max': 4918
        },
        'campaign': {
            'min': 1,
            'max': 63,
        },
        'pdays': {
             'min':-1,
             'max':871
        },
        'previous': {
            'min':0,
            'max':275
        },
        'poutcome': values_list['poutcome'].classes_.tolist()
    }

# configure les paramètres par défaut de la page
st.set_page_config(layout="wide",  page_icon="🧊", page_title="Predict_crédit")

def main() -> bool:
    """
    Affichage de la page qui dépend de l'état de show_formulaire contenu dans session_state
    """
    # Initialisation de l'état de session
    if 'show_formulaire' not in st.session_state:
        # création de l'état de visualisation du formulaire
        st.session_state.show_formulaire = True
    
    # Si vrai, renvoie le formulaire, sinon renvoie la réponse
    if st.session_state.show_formulaire:
        # affiche le formulaire, une fois le bouton cliqué, appel l'API et modifie l'état de show_formulaire en False
        formulaire(values)
    else:
        # affiche la réponse de la prédiction après appel de l'API et passage de l'état de show_formulaire en False
        # un bouton permet de faire une nouvelle prédiction et de réinitialiser l'état de show_formulaire en True
        response()
    return True

if __name__ == "__main__":
    main()




