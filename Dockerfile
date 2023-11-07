FROM continuumio/miniconda3

WORKDIR /home/app/

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files into the container
COPY . .

RUN pytest test.py || exit 1

CMD python3 train.py
