from fastapi import FastAPI
import uvicorn
import functions

app = FastAPI(
    title="API prédictions accords bancaire",
    descrtiption="""
Descritption de l'api ici !!!
"""
)

# Définir une route POST pour la commande
@app.get("/predict")
def predict(n:dict):
    transform = functions.scal_lab(n)
    prediction= functions.predictions(transform)
    return prediction.json()

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
