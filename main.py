from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Cassy !"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Bonjour, {name} !"}

@app.get("/addition")
def addition(a: int, b: int):
    return {"résultat": a + b}

class Utilisateur(BaseModel):
    nom: str
    age: int

@app.post("/utilisateur")
def creer_utilisateur(utilisateur: Utilisateur):
    return {
        "message": f"Utilisateur {utilisateur.nom} créé avec succès.",
        "données": utilisateur
    }

@app.put("/utilisateur/{nom}")
def mettre_a_jour_utilisateur(nom: str, utilisateur: Utilisateur):
    return {
        "message": f"{nom} mis à jour en {utilisateur.nom}, {utilisateur.age} ans."
    }

@app.delete("/utilisateur/{nom}")
def supprimer_utilisateur(nom: str):
    return {"message": f"Utilisateur {nom} supprimé."}
