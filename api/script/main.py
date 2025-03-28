import pymongo
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
client = pymongo.MongoClient("mongodb://root:example@mongo:27017/")
db = client.Projet
collection = db.pokemon

# Configurez CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Remplacez par les origines autorisées
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les en-têtes
)

@app.get("/")
def read_root():
    return {"Hello": "VueJS"}

@app.get("/dex/{dex_num}",description="Search a Pokemon by his dex number")
def search_by_dex(dex_num:int):
    objet=collection.find_one({"dex":dex_num},{"_id":0})
    return objet

@app.get("/pokemon/{poke_name}",description="Search a Pokemon by his name")
def search_by_name(poke_name:str):
    objet=collection.find_one({"name": {"$regex": f"^{poke_name}$", "$options": "i"}}, {"_id": 0})
    return objet

@app.get("/types/{poke_type}",description="Search which Pokemon share a type")
def search_by_type(poke_type:str):
    objets = collection.find(
        {"forms": {"$elemMatch": {"types": str.upper(poke_type)}}},  # Recherche dans la liste
        {"_id": 0, "name" : 1}
    )
    return list(objets)