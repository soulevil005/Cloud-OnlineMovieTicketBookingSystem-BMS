from fastapi import APIRouter
from app.models import Seat
from app.database import seat_collection

router = APIRouter()

# Add seats
@router.post("/add-seat")
def add_seat(seat: Seat):
    seat_collection.insert_one(seat.dict())
    return {"message": "Seat added"}

# Lock seat
@router.post("/lock-seat")
def lock_seat(movie_name: str, seat_number: str):
    seat = seat_collection.find_one({
        "movie_name": movie_name,
        "seat_number": seat_number
    })

    if not seat:
        return {"message": "Seat not found"}

    if seat["status"] == "available":
        seat_collection.update_one(
            {"movie_name": movie_name, "seat_number": seat_number},
            {"$set": {"status": "locked"}}
        )
        return {"message": "Seat locked"}

    return {"message": "Seat already booked or locked"}

# View seats
@router.get("/seats")
def get_seats():
    seats = list(seat_collection.find({}, {"_id": 0}))
    return seats