from pydantic import BaseModel

class Theatre(BaseModel):
    name: str
    location: str
    movie_name: str
    show_time: str