import json
import paho.mqtt.client as mqtt
import pymongo
import time
import msgParser
from service import *
import psutil
import os
from dotenv import load_dotenv

load_dotenv()



db = None
# Database Conncection
try:
    db = pymongo.MongoClient("mongodb://WiserMachines:W*123123*M@13.234.35.190:27017/WiserMachines?authSource=WiserMachines")
    # db = pymongo.MongoClient("mongodb://localhost:27017")

    db = db["WiserMachines"]
    print("Database connected succesfully")
except Exception as e:
    print(e)


message_flag = False

#call backs

def on_connect(client,userData,flags,rc):
    if(rc==0):
        print("Connected Successfully")

        client.subscribe("StatusUpdates",qos=0)

def on_message(client, userdata, message):
    # print("received message: " ,message.payload[6])
    try:
        message = message.payload
        parser= msgParser.Parser()
        parsed_message = parser.decipher_message(message)
        data = getAlertData(parsed_message,db)
        client.publish("Environment_Alert_Data",json.dumps(data))
        del data
        print('RAM memory % used:', psutil.virtual_memory()[2])
        
    except Exception as e:
        print(e)


def on_publish(client,userdata,result):
    print("Data Published for Environment")

client = mqtt.Client(client_id="Alert_Socket_Python")
client.on_message = on_message
client.on_publish = on_publish
client.on_connect = on_connect
client.connect(os.getenv("mqtt_client"),int(os.getenv("mqtt_host")),int(os.getenv("time_alive")))
client.loop_forever()


   










