import pymongo
import json
import os

from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
db = client.Projet
collection = db.pokemon
requesting = []

for file in os.listdir('Pokemon'):
    print(file)
    with open(os.path.join("Pokemon", file)) as f:
        data = f.read()
        myDict = json.loads(data)
        requesting.append(InsertOne(myDict))
    



result = collection.bulk_write(requesting)
client.close()

#print(os.listdir("./"))