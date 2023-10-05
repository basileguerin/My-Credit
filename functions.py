import streamlit as st
from streamlit_echarts import st_echarts
import joblib
import requests
import pandas as pd

def formulaire():
    # récupération du dictionnaire de labelencoders
    values_list = joblib.load('encoders')

    # Titre de la page
    st.write("<h1 style='text-align: center; margin: 0 0 25px 0'>Prédiction d'acceptation de crédit</h1>", unsafe_allow_html=True)

    # Divisez la mise en page en deux colonnes
    col1, col2, col3 = st.columns(3)

    # Colonne 1
    with col1:
        age = st.slider("Sélectionnez l'âge", min_value=18, max_value=95, step=1, help='toto')
        job = st.selectbox("Sélectionnez l'emploi", values_list['job'].classes_.tolist())
        marital = st.selectbox("Sélectionnez l'état civil", values_list['marital'].classes_.tolist())
        education = st.selectbox("Sélectionnez le niveau d'étude", values_list['education'].classes_.tolist())
        balance = st.number_input("Saisissez votre solde", min_value=-8019, max_value=1021270, step=1, value=0)      

    # Colonne 2
    with col2:
        default = st.checkbox("Le crédit est-il en défaut ?")  
        housing = st.checkbox("Un prêt logement a-t-il été contracté ?")
        loan = st.checkbox('Un prêt personnel a-t-il été contracté ?')
        contact = st.selectbox("Type de communication du contact ?",  values_list['contact'].classes_.tolist())
        day = st.slider("Dernier jour du contact du mois ?", min_value=1, max_value=31, step=1)
        month = st.selectbox("Dernier mois de contact de l'année ?",  values_list['month'].classes_.tolist())              

    # Colonne 3
    with col3:       
        duration = st.number_input("Durée du dernier contact, en secondes", min_value=0, max_value=4918, step=1)  
        campaign = st.number_input('Nombre de contacts effectués pendant cette campagne', min_value=1, max_value=63, step=1)
        pdays = st.number_input("Nombre de jours écoulés après que le client a été contacté pour la dernière fois lors d'une campagne précédente", min_value=-1, max_value= 871 ,  step=1)
        previous = st.number_input('Nombre de contacts effectués avant cette campagne et pour ce client', min_value=0, max_value= 275, step=1)
        poutcome = st.selectbox('Résultat de la campagne marketing précédente', values_list['poutcome'].classes_.tolist())

    col1bis, col2bis, col3bis = st.columns([0.45, 0.1, 0.45])

    with col1bis:
            st.write("")

    with col2bis:
        # Bouton pour soumettre le formulaire
        if st.button("Soumettre"):  
            data_json = {"age": age, "job": job, "marital": marital, "education": education, "default": 'yes' if default else 'no', 
            "balance": balance, "housing": 'yes' if housing else 'no', "loan": 'yes' if loan else 'no', "contact": contact, "day": day, "month": month,
            "duration": duration, "campaign": campaign, "pdays": pdays, "previous": previous, "poutcome": poutcome}

            st.session_state.donnees_formulaire = data_json     

            response = requests.post('https://api-isen-g1-46331383ef49.herokuapp.com/predict', json= data_json)
            st.session_state.response = response.json()
 
            # Rediriger vers la page de réponse en masquant le formulaire
            st.session_state.show_formulaire = False 

            st.rerun()
        
    with col3bis:
            st.write('')
     

def response():        
        # affichage du graphique    
        option = {
            "tooltip": {
                "formatter": '{a} <br/>{b} : {c}%'
            },
            "series": [{
                "name": '',
                "type": 'gauge',
                "startAngle": 180,
                "endAngle": 0,
                "progress": {
                    "show": "true"
                },
                "radius":'100%', 

                "itemStyle": {
                    "color": '#58D9F9',
                    "shadowColor": 'rgba(0,138,255,0.45)',
                    "shadowBlur": 10,
                    "shadowOffsetX": 2,
                    "shadowOffsetY": 2,
                    "radius": '55%',
                },
                "progress": {
                    "show": "true",
                    "roundCap": "true",
                    "width": 15
                },
                "pointer": {
                    "length": '60%',
                    "width": 8,
                    "offsetCenter": [0, '5%']
                },
                "detail": {
                    "valueAnimation": "true",
                    "formatter": '{value}%',
                    "backgroundColor": '#58D9F9',
                    "borderColor": '#999',
                    "borderWidth": 4,
                    "width": '60%',
                    "lineHeight": 20,
                    "height": 20,
                    "borderRadius": 188,
                    "offsetCenter": [0, '40%'],
                    "valueAnimation": "true",
                },
                "data": [{
                    #récupère la valeur de la réponse stockée dans l'état pour l'afficher
                    "value": st.session_state['response']['proba'],
                    "name": "Probabilité d'acceptation"
                }]
            }]
        };

        # Titre de la page
        st.write("<h1 style='text-align: center; margin: 0 0 25px 0'>Réponse de l'acceptation de crédit</h1>", unsafe_allow_html=True)
        st_echarts(options=option)
        st.write(f'<div style="text-align:center; font-size: 30px">Réponse: {"Pas accepté" if st.session_state["response"]["reponse"] == "no" else "Accepté"}</div>', unsafe_allow_html=True)

        # Divisez la mise en page en trois colonnes
        col1_df, col2_df, col3_df = st.columns([0.18, 0.64, 0.18])

        with col1_df:
             st.write('')

        with col2_df:    
            st.write('')
 
            # génération du graphique à partir d'un dataframe créer à partir de la réponse stocké dans st.session_state
            st.write('<div style="text-align:center; font-size: 25px">Importance des features dans la prédiction</div>', unsafe_allow_html=True)
            df = pd.DataFrame({'keys':st.session_state['response']['importance'][0], 'values':st.session_state['response']['importance'][1]})    
            st.bar_chart(df.set_index('keys'))

        with col3_df:
             st.write('')

        # Divisez la mise en page en trois colonnes
        col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

        with col1:
             st.write('')

        with col2:
            # recharge la page pour une nouvelle prédiction
            if st.button("Recharger la page"):
                st.session_state.show_formulaire = True
                st.rerun()

        with col3:
             st.write('')