import joblib
import numpy as np
from pydantic import BaseModel
import os
import mlflow
import boto3

# # importer le modèle, les scaler et les labelencoder
enc = joblib.load("encoders")
scal = joblib.load("scalers")

# Recupértation du modèle sur MlFlow
os.environ['AWS_ACCESS_KEY_ID'] = "AKIA3R62MVALHESATEYJ"
os.environ['AWS_SECRET_ACCESS_KEY'] = "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"
mlflow.set_tracking_uri("https://isen-mlflow-fae8e0578f2f.herokuapp.com/")
logged_model = 'runs:/6ef80807a5774935978d92bdd6b18250/My-Credit'
model = mlflow.sklearn.load_model(logged_model)

# Configuration d'une classe BaseModel pour s'assurer que les 
# données correspondent bien avec ce qui est attendu
class Config_donnees(BaseModel):
    age:int
    job:str
    marital:str
    education:str
    default:str
    balance:int
    housing:str
    loan:str
    contact:str
    day:int
    month:str
    duration:int
    campaign:int
    pdays:int
    previous:int
    poutcome:str

class reponse_model(BaseModel):
    reponse:str
    proba:float
    importance:list


def scal_lab(n:dict) ->list:
    """
    Fonction servant à standardiser et labéliser les donnees
    Entrée json
    Sortie de type : [0.12,0.55,0.56....]
    """
    transformed_data=[]
    
    transformed_data.append(scal['age'].transform(np.array([n.age]).reshape(-1, 1))[0][0])
    job = enc['job'].transform([n.job])[0]
    transformed_data.append(scal['job'].transform(np.array([job]).reshape(-1,1))[0][0])
    marital = enc['marital'].transform([n.marital])[0]
    transformed_data.append(scal['marital'].transform(np.array([marital]).reshape(-1,1))[0][0])
    education = enc['education'].transform([n.education])[0]
    transformed_data.append(scal['education'].transform(np.array([education]).reshape(-1,1))[0][0])
    default = enc['default'].transform([n.default])[0]
    transformed_data.append(scal['default'].transform(np.array([default]).reshape(-1,1))[0][0])
    transformed_data.append(scal['balance'].transform(np.array([n.balance]).reshape(-1, 1))[0][0])
    housing= enc['housing'].transform([n.housing])[0]
    transformed_data.append(scal['housing'].transform(np.array([housing]).reshape(-1,1))[0][0])
    loan = enc['loan'].transform([n.loan])[0]
    transformed_data.append(scal['loan'].transform(np.array([loan]).reshape(-1,1))[0][0])
    contact = enc['contact'].transform([n.contact])[0]
    transformed_data.append(scal['contact'].transform(np.array([contact]).reshape(-1,1))[0][0])
    transformed_data.append(scal['balance'].transform(np.array([n.day]).reshape(-1, 1))[0][0])
    month = enc['month'].transform([n.month])[0]
    transformed_data.append(scal['month'].transform(np.array([month]).reshape(-1,1))[0][0])
    transformed_data.append(scal['duration'].transform(np.array([n.duration]).reshape(-1, 1))[0][0])
    transformed_data.append(scal['campaign'].transform(np.array([n.campaign]).reshape(-1, 1))[0][0])
    transformed_data.append(scal['pdays'].transform(np.array([n.pdays]).reshape(-1, 1))[0][0])
    transformed_data.append(scal['previous'].transform(np.array([n.previous]).reshape(-1, 1))[0][0])
    poutcome=enc['poutcome'].transform([n.poutcome])[0]
    transformed_data.append(scal['poutcome'].transform(np.array([poutcome]).reshape(-1,1))[0][0])
    return transformed_data

def predictions(data:list) -> dict:
    """
    Fonction permettant la prédiction et l'inversement de labélisation
    Sortie de type : {'reponse':'no','proba':99.99,'importance':[['age',...'poutcome],[0.12,...,0.005]]}
    """

    # Prédiction en utilisant le modèle
    data = np.array([data])
    result = model.predict(data)
    proba = model.predict_proba(data)
    pred = enc['y'].inverse_transform(result)[0]

    # Bonus importances des features
    liste_features = ["age", "job", "marital", "educations", "default", "balance",
                 "housing", "loan", "contact", "day", "month", "duration",
                 "camapaign", "pdays", "previous", "poutcome"]
    probs = model.feature_importances_
    probs_list=[float(i) for i in probs]

    # Renvoi du dictionnaire contenant la prédiction, la probabilité d'un oui
    # et une liste avec la liste des variables et la liste des probabilités
    return {'reponse':pred,
            'proba':round(proba[0][1]*100,2),
            'importance':[liste_features,probs_list]}

