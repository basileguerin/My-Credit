import streamlit as st
from functions import *  

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
        formulaire()
    else:
        # affiche la réponse de la prédiction après appel de l'API et passage de l'état de show_formulaire en False
        # un bouton permet de faire une nouvelle prédiction et de réinitialiser l'état de show_formulaire en True
        response()
    return True

if __name__ == "__main__":
    main()




