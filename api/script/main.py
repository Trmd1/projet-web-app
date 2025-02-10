import pymongo
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient

app = FastAPI()
client = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
db = client.Projet
collection = db.pokemon

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/dex/{dex_num}")
def search_dex(dex_num:int):
    objet=collection.find_one({"dex":dex_num},{"_id":0})
    return objet

@app.get("/pokemon/{poke_name}")
def search_name(poke_name:str):
    objet=collection.find_one({"name": {"$regex": f"^{poke_name}$", "$options": "i"}}, {"_id": 0})
    # print(collection.find_one({"dex":0},{"_id":0})["name"])
    # boolTest = False
    # boolTest = (str.lower(poke_name)==str.lower(collection.find_one({"dex":0},{"_id":0})["name"]))
    # print(boolTest)
    return objet