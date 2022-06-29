import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")

db = db["WiserMachinesTest"]
mycol = db["data"]

x = mycol.find().limit(1)

for y in x:
    print (y)