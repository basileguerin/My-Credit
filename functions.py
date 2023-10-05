import joblib
import numpy as np
from pydantic import BaseModel


# # importer le modèle, les scaler et les labelencoder
enc = joblib.load("encoders")
model = joblib.load("model")
scal = joblib.load("scalers")

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


def scal_lab(n:dict) ->list:
    """
    Fonction servant à standardiser et labéliser les donnees
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
    print("!!!!!!!!!!!!!!!!!!!!!!", transformed_data)
    return transformed_data

def predictions(data:list) -> dict:
    """
    Fonction permettant la prédiction et l'inversement de labélisation
    Sortie de type : {'reponse':'no','proba':99.99}
    """
    data = np.array([data])
    result = model.predict(data)
    proba = model.predict_proba(data)
    pred = enc['y'].inverse_transform(result)[0]
    return {'reponse':pred,'proba':round(proba[0][1]*100,2)}

