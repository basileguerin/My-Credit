import streamlit as st
from streamlit_echarts import st_echarts
import requests
import pandas as pd


def formulaire(values: dict) -> bool:
    '''
    Formulaire qui recueille les données nécessaires pour la prédiction.  
    '''

    # Titre de la page
    st.write("<h1 style='text-align: center; margin: 0 0 25px 0'>Prédiction d'acceptation de crédit</h1>",
             unsafe_allow_html=True)

    # *******Première partie de la page
    # Gère l'affichage du formulaire en trois colonnes de taille identique
    col1, col2, col3 = st.columns(3)

    # Colonne 1
    with col1:
        age = st.slider("Sélectionnez l'âge",
                        min_value=values['age']['min'],
                        max_value=values['age']['max'],
                        step=1)
        # génération des options à partir du dictionnaire extrait de encoders
        job = st.selectbox("Sélectionnez l'emploi",
                           values['job'])
        marital = st.radio("Sélectionnez l'état civil",
                           horizontal=True,
                           options=values['marital'],
                           help=' "divorced" signifie divorcé ou veuf')
        education = st.radio("Sélectionnez le niveau d'étude",
                             horizontal=True,
                             options=values['education'])
        balance = st.number_input("Saisissez votre solde",
                                  step=1,
                                  value=0)

    # Colonne 2
    with col2:
        # input qui renvoie True si coché, sinon False par défaut
        default = st.toggle("Le crédit est-il en défaut ?")
        housing = st.toggle("Un prêt logement a-t-il été contracté ?")
        loan = st.toggle('Un prêt personnel a-t-il été contracté ?')
        contact = st.radio("Type de communication du contact ?",
                           horizontal=True,
                           options=values['contact'])
        day = st.slider("Dernier jour du contact du mois ?",
                        min_value=values['day']['min'],
                        max_value=values['day']['max'],
                        step=1)
        month = st.selectbox("Dernier mois de contact de l'année ?",
                             values['month'])

    # Colonne 3
    with col3:
        duration = st.number_input("Durée du dernier contact, en secondes",
                                   step=1,
                                   value=0)
        campaign = st.number_input('Nombre de contacts effectués pendant cette campagne',
                                   step=1,
                                   value=1)
        pdays = st.number_input("Nombre de jours écoulés après que le client a été contacté pour la dernière fois lors d'une campagne précédente",
                                step=1,
                                value=-1,
                                help="-1 signifie que le client n'a pas été contacté auparavant")
        previous = st.number_input('Nombre de contacts effectués avant cette campagne et pour ce client',
                                   step=1,
                                   value=0)
        poutcome = st.radio('Résultat de la campagne marketing précédente',
                            horizontal=True,
                            options=values['poutcome'])

    # *******Deuxième partie de la page
    # permet de centrer le bouton au milieu de la page
    col1bis, col2bis, col3bis = st.columns([0.38, 0.24, 0.38])

    # colonne 1 (vide)
    with col1bis:
        st.write("")

    # colonne 2: affichage du bouton qui permet de valider le formulaire
    with col2bis:
        # création du dictionnaire à envoyer dans la réponse
        data_json = {
            "age": age,
            "job": job,
            "marital": marital,
            "education": education,
            # modifie le boolean en réponse conforme pour l'API
            "default": correction_param(default),
            "balance": balance,
            "housing": correction_param(housing),
            "loan": correction_param(loan),
            "contact": contact,
            "day": day,
            "month": month,
            "duration": duration,
            "campaign": campaign,
            "pdays": pdays,
            "previous": previous,
            "poutcome": poutcome
        }
        conditions_values(balance, duration, campaign,
                          pdays, previous, values, data_json)

    # colonne 3 (vide)
    with col3bis:
        st.write('')

    return True


def response() -> bool:
    """
    Affichage de la réponse une fois la prédiction réalisée
    """
    # options du graphique
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
            "radius": '100%',

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
                # récupère la valeur de la réponse stockée dans l'état pour l'afficher
                "value": st.session_state['response']['proba'],
                "name": "Probabilité d'acceptation"
            }]
        }]
    }

    st.write("<h1 style='text-align: center; margin: 0 0 25px 0'>Réponse de l'acceptation de crédit</h1>",
             unsafe_allow_html=True)

    # *******Première partie de la page
    # Permet de centrer les différents widgets au centre de la page
    col1_df, col2_df = st.columns([0.4, 0.6])

    # colonne 1 (vide)
    with col1_df:
        # créé un espace vide au dessus du graphique
        st.write(
            f'<div style="height: 100px"></div>', unsafe_allow_html=True)
        # affichage graphique
        st_echarts(options=option)

        # background-color suivant la réponse de la prédiction
        if st.session_state["response"]["reponse"] == "no":
            color = 'red'
            response = 'Crédit refusé'
        else:
            color = '#b2d8b2'
            response = 'Crédit accepté'
        st.write(f'<div style="text-align:center; font-size: 30px; background-color: {color}; border-radius: 15px">Réponse: {response} </div>',
                 unsafe_allow_html=True)
    # colonne 2, graphique précisant les features ayant le plus d'importance dans la prédiction
    with col2_df:
        st.write('')

        st.write("<div style='text-align:center; font-size: 25px'>Données envoyées pour la prédiction</div>",
                 unsafe_allow_html=True)
        # affichage des données soumises pour la prédiction sous forme de dataframe
        df_form = pd.DataFrame.from_dict([st.session_state.formulaire])
        st.write(df_form)

        st.write('<div style="text-align:center; font-size: 25px">Importance des features dans la prédiction</div>', unsafe_allow_html=True)
        # génération d'un dataframe avec la réponse renvoyé par l'API et stockké dans session_state
        df = pd.DataFrame({'keys': st.session_state['response']['importance']
                          [0], 'values': st.session_state['response']['importance'][1]})
        # génération d'un graphique à barre à partir du dataframe
        st.bar_chart(df.set_index('keys'))

    # *******Seconde partie de la page
    # Permet de centrer le bouton
    col1, col2, col3 = st.columns([0.45, 0.1, 0.45])

    # colonne 1 (vide)
    with col1:
        st.write('')

    # colonne 2, affichage du bouton
    with col2:
        # recharge la page pour une nouvelle prédiction
        if st.button("Faire une nouvelle prédiction"):
            st.session_state.show_formulaire = True
            st.rerun()

    # colonne 3 (vide)
    with col3:
        st.write('')

    return True


def api_predict(data_json: dict) -> dict:
    """
    appel de l'API pour faire la prédiction
    :data_json: réponse du formulaire organisée sous forme de dictionnaire dans le même ordre que l'apparition du dataframe
    """
    response = requests.post(
        'https://api-isen-g1-46331383ef49.herokuapp.com/predict', json=data_json)
    return response.json()


def correction_param(param: bool) -> str:
    """
    transforme le boolean en string yes or no
    :param: boolean issus du checkbox du formulaire
    """
    return 'yes' if param else 'no'


def conditions_values(balance: int, duration: int, campaign: int, pdays: int, previous: int, values: dict, data_json: dict) -> bool:
    """
    Bloque la validation si une valeur d'un des paramètres se trouve en dehors des valeurs min et max
    :balance, duration, campaign, pdays, previous proviennent du formulaire des input numbers
    :values, dictionnaire qui rassembles valeurs min et max, ou les options des paramètres
    :data_json, dictionnaire qui rassemble toutes les valeurs collectées par le formulaire
    """

    if balance > values['balance']['max'] or balance < values['balance']['min']:
        if st.button("Soumettre"):
            st.write(
                f'La valeur balance doit être comprise entre {values["balance"]["min"]} et {values["balance"]["max"]}')
        return True
    elif duration > values['duration']['max'] or duration < values['duration']['min']:
        if st.button("Soumettre"):
            st.write(
                f'La valeur duration doit être comprise entre {values["duration"]["min"]} et {values["duration"]["max"]}')
        return True
    elif campaign > values['campaign']['max'] or campaign < values['campaign']['min']:
        if st.button("Soumettre"):
            st.write(
                f'La valeur campaign doit être comprise entre {values["campaign"]["min"]} et {values["campaign"]["max"]}')
        return True
    elif pdays > values['pdays']['max'] or pdays < values['pdays']['min']:
        if st.button("Soumettre"):
            st.write(
                f'La valeur pdays doit être comprise entre {values["pdays"]["min"]} et {values["pdays"]["max"]}')
        return True
    elif previous > values['previous']['max'] or previous < values['previous']['min']:
        if st.button("Soumettre"):
            st.write(
                f'La valeur previous doit être comprise entre {values["previous"]["min"]} et {values["previous"]["max"]}')
        return True

    else:
        # Bouton pour soumettre le formulaire
        if st.button("Soumettre"):

            # stockage de la réponse de l'API dans session_state
            st.session_state.formulaire = data_json
            st.session_state.response = api_predict(data_json)

            # Redirection vers la page de réponse en masquant le formulaire
            st.session_state.show_formulaire = False
            st.rerun()
            return True
