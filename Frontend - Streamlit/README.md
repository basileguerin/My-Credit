# Application Front Streamlit

## Introduction
L'application recueille les données via un formulaire et renvoie les données réceptions sous forme de graphique et d'une réponse écrite de la réponse de la prédiction. 

## Explication
En accueil, un formulaire qui permet de reccueillir les données pour la prédiction. <br>
Les options proposées proviennent des encoders générés lors de l'entraînement du modèle. <br>
Les données sont envoyées en brut en JSON. <br>
Une fois la prédiction faite, via une API stocké sur Heroku, la réponse apparait. <br>
Un graphique donnant le pourcentage de réponse positive apparait, ainsi qu'une réponse écrite. <br>
Un graphique présente les features ayant le plus d'importance.

## Liens
lien vers streamlit : https://my-credit-g7xraeyumygdlnn6ch9zu2.streamlit.app/ <br>
lien vers l'API: https://api-isen-g1-46331383ef49.herokuapp.com/docs <br>
lien vers MLFlow: https://isen-mlflow-fae8e0578f2f.herokuapp.com/#/experiments/29/runs/1c4629fd398a43ae9a1c5e5d26e166ab