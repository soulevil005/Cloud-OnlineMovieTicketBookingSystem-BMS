from fastapi import APIRouter
from database import booking_collection
from models import Booking

router = APIRouter()

@router.post("/book")
def book_ticket(booking: Booking):
    booking_collection.insert_one(booking.dict())
    return {"message": "Booking successful"}

@router.get("/bookings")
def get_bookings():
    bookings = list(booking_collection.find({}, {"_id": 0}))
    return bookings