from fastapi import APIRouter
from app.models import Movie
from app.database import movie_collection   

router = APIRouter()

# Add movie
@router.post("/add-movie")
def add_movie(movie: Movie):
    movies_collection.insert_one(movie.dict())
    return {"message": "Movie added successfully"}

# Get all movies
@router.get("/movies")
def get_movies():
    movies = list(movies_collection.find({}, {"_id": 0}))
    return movies