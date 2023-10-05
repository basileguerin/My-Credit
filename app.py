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
@app.post("/predict", response_model=functions.reponse_model, summary="Prédictions")
def predict(n:functions.Config_donnees):
    """
    Obtenez un avis de prêt bancaire en utilisant les paramètres suivants:
    - **age**:30,
    - **job**:"services",
    - **marital**:"married",
    - **education**:"tertiary",
    - **default**:"no",
    - **balance**:1350,
    - **housing**:"yes",
    - **loan**:"no",
    - **contact**:"cellular",
    - **day**:16,
    - **month**:"oct",
    - **duration**:185,
    - **campaign**:1,
    - **pdays**:330,
    - **previous**:1,
    - **poutcome**:"other"
    ### reponse est égale à 'yes' ou 'no'
    ### proba correspond à la probabilité d'acceptation du dossier
    """
    transform = functions.scal_lab(n)
    prediction= functions.predictions(transform)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$",prediction)
    return prediction

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
