from fastapi import APIRouter
from app.models import Theatre
from app.database import theatre_collection

router = APIRouter()

@router.post("/add-theatre")
def add_theatre(theatre: Theatre):
    theatre_collection.insert_one(theatre.dict())
    return {"message": "Theatre added"}

@router.get("/theatres")
def get_theatres():
    return list(theatre_collection.find({}, {"_id": 0}))