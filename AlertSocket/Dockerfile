FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt

CMD ["python3","alert_socket.py"]