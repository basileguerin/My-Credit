FROM  continuumio/miniconda3

WORKDIR /home/app

RUN pip install streamlit joblib streamlit_echarts pandas scikit-learn

COPY . /home/app

CMD streamlit run app.py --server.port $PORT

#commande pour lancer le dockerfile
# docker build . -t streamlit
# docker images => voir toutes les images
# docker run -it -v "$(pwd):/home/app" streamlit bash => envoie les fichiers sur le conteneur et ouvre le bash du conteneur
# docker run -it -p "80:$PORT" -v "$(pwd):/home/app" -e PORT=$PORT streamlit => lance l'application dans le conteneur sur localhost:80