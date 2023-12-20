from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

# Lista de users creada apartir de la entidad User
users_list = [User(name="Omar", surname="Alvarado", url="https://omar.com", age=21),
              User(name="Juan", surname="Perez", url="https://juan.com", age=35),
              User(name="Maria",surname="Lopez", url="https://maria.com", age=28)]    

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1, "name": "John"}, 
            {"id": 2, "name": "Mary"},
            {"id": 3, "name": "Omar"}]

# Endpoint para obtener la lista de users
@app.get("/users")
async def users():
    return users_list



