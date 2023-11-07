from fastapi import FastAPI
import uvicorn
import functions

# Config apparence API
descritpion ="""
    Obtenez un avis de prêt bancaire en utilisant les paramètres suivants:
    - age: int
    - job: str ['admin.' 'blue-collar' 'entrepreneur' 'housemaid' 'management' 'retired' 'self-employed' 'services' 'student' 'technician' 'unemployed' 'unknown'] 
    - marital: str ['divorced' 'married' 'single'] 
    - education: str ['primary' 'secondary' 'tertiary' 'unknown']
    - default: str ['no' 'yes'] 
    - balance: int 
    - housing: str ['no' 'yes'] 
    - loan: str ['no' 'yes']
    - contact: str ['cellular' 'telephone' 'unknown'] 
    - day: int 
    - month: str ['apr' 'aug' 'dec' 'feb' 'jan' 'jul' 'jun' 'mar' 'may' 'nov' 'oct' 'sep'] 
    - duration: int
    - campaign: int
    - pdays: int 
    - previous: int
    - poutcome: str ['failure' 'other' 'success' 'unknown']
    """
app = FastAPI(
    title="API prédictions accords bancaire",
    summary="Api développée par Kevin LE GRAND en colaboration avec Basile GUERIN et Mickeal MARCOTTE",
    description=descritpion
)


# Définir une route POST pour la commande
@app.post("/predict", response_model=functions.reponse_model, summary="Prédictions")
def predict(n:functions.Config_donnees):
    """
    ## La réponse est de type json : {'reponse':'no','proba':0.99,'importance':[['age',...'poutcome'][0.12,...0.03]]}
    ### reponse est égale à 'yes' ou 'no'
    ### proba correspond à la probabilité d'acceptation du dossier
    ### importance comporte deux liste :
    - ### la liste des varibales 
    - ### la liste du pourcentage d'importance
    """
    # Appel de la fonction servant la encoder et standardiser
    transform = functions.scal_lab(n)
    # Appel de la fonction servant à réaliser les prédictions
    prediction= functions.predictions(transform)
    # Réponse au format json
    return prediction


if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=4000)
