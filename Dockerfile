# Utilisez l'image continuumio/miniconda3 comme image de base
FROM continuumio/miniconda3

# Définissez le répertoire de travail
WORKDIR /home/app

# Recuperation du repo
RUN git clone --branch Back https://github.com/basileguerin/My-Credit .

# Copiez les fichiers nécessaires
COPY requirements.txt .

# Installez les dépendances
RUN pip install -r requirements.txt

COPY . .

# Installez les outils nécessaires pour les tests (par exemple, pytest)
RUN pip install pytest

# Exécutez les tests et capturez le code de sortie
RUN pytest test.py || exit 1

# Exécutez votre application
CMD uvicorn app:app --host=0.0.0.0 --port=$PORT




# FROM continuumio/miniconda3

# WORKDIR /home/app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# CMD uvicorn app:app --host=0.0.0.0 --port=$PORT 


# docker run -it fastapi bash : bash permet de rentrer dasn le container
# docker build . -t fastapi : construction de l'image streamlit
# docker ps -a : pour voir tous les conteainer qui ont été créé
# docker run -it -v "C:\Users\utilisateur\Documents\GitHub\My-Credit:/home/app" fastapi bash : permet de connecter le repertoire courant avec le container

# Ports mapping
# docker run -it -p "80:4000" streamlit : connecté sur le port 4000 dans le container et sur le port 80 en local
 
#docker run -it -p 4000:$PORT -v "C:\Users\utilisateur\Documents\GitHub\My-Credit:/home/app" -e PORT=$PORT fastapi

# build : image
# run : container
# - v : volume