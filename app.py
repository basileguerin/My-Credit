import streamlit as st
from functions import *  

st.set_page_config(layout="wide",  page_icon="🧊", page_title="Predict",)

# Définir la disposition de l'application
def main():
    # Initialisation de l'état de session
    if 'show_formulaire' not in st.session_state:
        st.session_state.show_formulaire = True
    
    if st.session_state.show_formulaire:
        formulaire()
    else:
        response()

if __name__ == "__main__":
    main()




