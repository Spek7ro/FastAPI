from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista de users creada apartir de la entidad User
users_list = [User(id=1,name="Omar", surname="Alvarado", url="https://omar.com", age=21),
              User(id=2,name="Juan", surname="Perez", url="https://juan.com", age=35),
              User(id=3,name="Maria",surname="Lopez", url="https://maria.com", age=28)]    

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1, "name": "John"}, 
            {"id": 2, "name": "Mary"},
            {"id": 3, "name": "Omar"}]

# Endpoint para obtener la lista de users
@app.get("/users")
async def users():
    return users_list

# Obtener un user pasando el id como parametro 
# path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Obtener un user por query
# eje: http://localhost:8000/userquery/?id=1
@app.get("/user/")
async def user(id: int):
    return search_user(id)

# Agregar un user por post
@app.post("/user/")
async def user(user: User):
    # validar si el user ya se existe
    if type(search_user(user.id)) == User:
        return {"Error": "El usuario ya existe"} 
    else:    
        users_list.append(user)
        return user         

# Actualizar a un user por put
@app.put("/user/")
async def user(user: User):
    found = False
    # Buscar el usuario 
    for index, saved_user in enumerate(users_list):
        if user.id == saved_user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"Error": "El usuario no existe"}
    else:
        return user      


# funcion para obtener a un user por id
def search_user(id: int):
    # Obtener el user 
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"Error": "No se ha encontrado el usuario"}    