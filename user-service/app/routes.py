from fastapi import APIRouter
from app.models import User
from app.database import users_collection

router = APIRouter()

@router.post("/register")
def register(user: User):
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    found = users_collection.find_one({
        "email": user.email,
        "password": user.password
    })
    if found:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}