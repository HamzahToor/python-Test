
#Get the base python image from DockerHub
FROM ubuntu:latest

#Specify the working directory which holds the application inside the image
WORKDIR /usr/app/src

#Copy the current folder which contains python source code to the Docker image under main.py
COPY main.py ./

RUN apt update
RUN apt install python2 -y


#Run the output program
CMD ["python3","./main.py"]

