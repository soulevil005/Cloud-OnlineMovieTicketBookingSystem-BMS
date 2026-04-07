from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    genre: str
    duration: int