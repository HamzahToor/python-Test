#Get the base python image from DockerHub
FROM python:latest

# Specify the working directory which holds the application inside the image
WORKDIR /usr/app/src

# Copy the current folder which contains python source code to the Docker image under main.py
COPY main.py ./

# Run the output program

CMD ["./main.py"]
