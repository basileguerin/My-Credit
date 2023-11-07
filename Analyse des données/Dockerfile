FROM continuumio/miniconda3

WORKDIR /home/app/

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/basileguerin/My-Credit.git --branch Model --single-branch .

RUN pip install -r requirements.txt

RUN python3 test.py

CMD python3 train.py
