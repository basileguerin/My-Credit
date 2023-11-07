import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def get_data(csv_path: str):
    """
    Retourne un dataframe à partir du chemin d'un fichier csv.
    """
    return pd.read_csv(csv_path, delimiter=';')

def standardize_labelize(df: pd.DataFrame):
    """
    A partir d'un dataframe donné, labélise les colonnes catégoriques et standardise l'ensemble des features.
    Retourne le dataframe modifié et des dictionnaires contenant les encoders et scalers utilisés.
    """
    scalers = {}
    encoders = {}
    non_numerical = df.select_dtypes(exclude=['number']).columns.to_list()
    features = df.drop('y', axis=1).columns
    for col in non_numerical:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    for col in features:
        scaler = StandardScaler()
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
        scalers[col] = scaler

    return df, scalers, encoders

def train_model(csv_train_path: str):
    """
    A partir du chemin d'un fichier csv contenant des données d'entraînement, cette fonction réalise toutes les étapes
    pour entraîner un RandomForestClassifier.
    Retourne le modèle entraîné ainsi que les dictionnaires contenant les scalers en encoders pour les test.
    """
    df = get_data(csv_train_path)
    df, scalers, encoders = standardize_labelize(df)
    X = df.drop('y', axis=1)
    y = df['y']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model, scalers, encoders, X, y

def test_model(csv_test_path: str, model: RandomForestClassifier, scalers: dict, encoders: dict):
    """
    A partir du chemin d'un fichier csv contenant des données de test, d'un modèle entraîné et des dictionnaires d'encoders et scalers;
    cette fonction print l'accuracy du modèle, une matrice de confusion et un classification report.
    """
    df = get_data(csv_test_path)
    for col, le in encoders.items():
        df[col] = le.transform(df[col])
    for col, scaler in scalers.items():
        df[col] = scaler.transform(df[col].values.reshape(-1, 1))
    X = df.drop('y', axis=1)
    y = df['y']
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    confusion_matrix_result = confusion_matrix(y, y_pred)
    classification_report_result = classification_report(y, y_pred)
    print(f"Accuracy : {accuracy}")
    print(f"Confusion Matrix :\n{confusion_matrix_result}")
    print(f"Classification Report :\n{classification_report_result}")

if __name__ == "__main__":
    model, scalers, encoders, _, _ = train_model("./train.csv")
    test_model("./test.csv", model, scalers, encoders)