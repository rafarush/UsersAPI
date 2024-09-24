from fastapi import FastAPI
from pydantic import BaseModel

# Se inicia server con: uvicorn users:app --reload
app = FastAPI()

# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

# Datos de Prueba
usersList = [User(id = 1, name = "Rafael", surname = "Garcia",age = 20),
           User(id = 2, name = "Ly", surname = "Gonzalez",age = 19),
           User(id = 3, name = "Pepe", surname = "Perez",age = 19),
           User(id = 4, name = "Pepe", surname = "Perez",age = 32),
           User(id = 5, name = "Nataly", surname = "Garcia",age = 50)]


# url local : http://127.0.0.1:8000/usersjson
@app.get("/usersjson")
async def usersjson():
    return [{"id":"1", "name":"Rafael", "surname" : "Garcia", "age": "20"},
            {"id":"2", "name":"Ly", "surname" : "Gonzalez", "age": "50"},
            {"id":"3", "name":"Nataly", "surname" : "Garcia", "age": "19"}]


# url local : http://127.0.0.1:8000/users
@app.get("/users")
async def users():
    return usersList


# Buscar user por id
def findUser(id: int):
    user = list(filter(lambda user: user.id == id, usersList))
    return user[0] if user else {"Message" : "No existe"}


#Path
# url local : http://127.0.0.1:8000/user/{id: str} Devuelve user por id 
@app.get("/user/{id}")
async def user(id: int):
    return findUser(id)


#Query
# url local : http://127.0.0.1:8000/userquery Devuelve user por id query form [http://127.0.0.1:8000/userquery/?id=x]
@app.get("/userquery/")
async def user(id: int):
    return findUser(id)


#Query
# url local : http://127.0.0.1:8000/userfullnamequery/?name=x&suername=x Devuelve user por nombre y apellido [Todos los tocayos xd]
@app.get("/userfullnamequery/")
async def usersByNameAndSurname(name: str, surname: str):
    return findUsersNameAndSurname(name, surname)


# Buscar user por nombre y apellido
def findUsersNameAndSurname(name: str, surname: str):
    userFinal =[]
    user = list(filter(lambda user: user.name == name, usersList))
    if user:
        userFinal = list(filter(lambda user: user.surname == surname, user))
    return userFinal if userFinal else {"Message" : "No existe"}
    


# Post
# Agregar datos
@app.post("/user/")
async def addUser(user: User):
    if type(findUser(user.id)) != User:
        usersList.append(user)
    else:
        return {"Error" : "Usuario ya existente"}
    

# Delete
# Borra un usuario
@app.delete("/user/")
async def deleteUser(user: User):
    if findUser(user.id) == user:
        usersList.remove(user)
    else:
        return {"Error" : "Usuario no existente"}
    
