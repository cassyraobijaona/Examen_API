from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello world"}


@app.get("/welcome/{name}")
async def say_welcome (name: str):
    return {"message": f"Welcome, {name} "}



@app.post("/students")
class students (
    reference : str ;
    firstName : str ;
    lastName : str ;
    age : int ;
)

def creer_students(students: Students):
    return {
        "message": f"Students {students.id}, {students.firstName},"
                   f"{students.lastName}, {students.age} créé avec succès.",
    }



@app.get("students")
def read_root():
    return {"message": f"Students {students.Students} contenu de la "
                       f"liste d'objets ."}

@app.put("/students/{reference}")
def mettre_a_jour_reference(reference: str, students: app):
    return {
        "message": f"{reference} mis à jour en {students.reference}, "
    }


