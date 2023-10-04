import joblib

# # importer le modèle, les scaler et les labelencoder
# with open("donnees.pickle", "rb") as fichier:
#     model = pickle.load(model)
#     scalerAge = pickle.load(scalerAge)
# ....

def scal_lab(n:dict) ->list:
    """
    Fonction servant à standardiser et labéliser les donner
    """
    transformed_data=[]
    # transformed_data.append(scalerAge.transform(n['age']))
    # transformed_data.append(labelencoderJob.transform(n['job']))
    # ...
    return transformed_data

def predictions(data:list) -> dict:
    """
    Fonction permettant la prédiction et l'inversement de labélisation
    """
    result = model.predict(data)
    pred = label_ouput.inverse_transform(result)
    return {'reponse':pred}

