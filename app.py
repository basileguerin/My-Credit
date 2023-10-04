from fastapi import FastAPI
import uvicorn
import functions
from pydantic import BaseModel

class config_donnees(BaseModel):
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

app = FastAPI(
    title="API prédictions accords bancaire",
    descrtiption="""
Descritption de l'api ici !!!
"""
)

# Définir une route POST pour la commande
@app.post("/predict")
def predict(n:config_donnees):
    print(n)
    transform = functions.scal_lab(n)
    prediction= functions.predictions(transform)
    return prediction.json()

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
