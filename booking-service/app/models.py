from pydantic import BaseModel

class Booking(BaseModel):
    user_email: str
    movie_name: str
    seats: list