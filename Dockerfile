FROM java:latest
COPY . /usr/src/app 
WORKDIR /usr/src/app 
RUN javac Hello.java  
CMD ["java", "Hello"]  
