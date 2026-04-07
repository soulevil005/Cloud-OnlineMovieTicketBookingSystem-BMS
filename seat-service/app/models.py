from pydantic import BaseModel

class Seat(BaseModel):
    movie_name: str
    seat_number: str
    status: str  # available / locked / booked