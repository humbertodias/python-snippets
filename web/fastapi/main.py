# python3 -m venv $HOME/venv
# source $HOME/venv/bin/activate
# python3 -m pip install fastapi uvicorn
# uvicorn main:app --reload
# http://127.0.0.1:8000/docs

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake database (in-memory)
users = []

class User(BaseModel):
    name: str

# GET all users
@app.get("/")
def get_all_users():
    return {"users": users}

# GET user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < len(users):
        return users[user_id]
    return {"error": "User not found"}

# POST create user
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}