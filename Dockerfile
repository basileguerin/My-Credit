FROM continuumio/miniconda3

WORKDIR /home/app/

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files into the container
COPY . .

# Set the shell script as the default command
CMD ["/home/app/entrypoint.sh"]
