from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId


user = APIRouter()

@user.get('/users')
def find_all_user():
    return usersEntity(conn.local.user.find())

@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    id =  conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)

@user.get('/users/{id}')
def find_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
    
@user.put('/users/{id}')
def update_user():
    return "Hello World"

@user.delete('/users/{id}')
def delete_user():
    return "Hello World"


    #43:12