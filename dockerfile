FROM python:3-alpine

# Create app directory
WORKDIR /app

# Copy the dependencies
COPY ./requirements.txt /app

# Install app dependencies
RUN pip install -r requirements.txt

# Copy all app files
COPY . .

# Expose the access port
EXPOSE 5000

# Set the enviroment runner
ENV FLASK_APP=project/server.py

# Initiaze start
CMD ["flask", "run", "--host", "0.0.0.0"]