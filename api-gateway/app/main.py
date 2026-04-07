from fastapi import FastAPI
import requests

app = FastAPI()

# ✅ YOUR DEPLOYED SERVICES
USER_SERVICE = "https://user-service-new-wzpd.onrender.com"
MOVIE_SERVICE = "https://movie-service-63iw.onrender.com"
BOOKING_SERVICE = "https://booking-service-ulkk.onrender.com"


@app.get("/")
def root():
    return {"message": "API Gateway Running"}


# ---------- USER ----------
@app.post("/register")
def register(data: dict):
    res = requests.post(f"{USER_SERVICE}/register", json=data)
    return res.json()


@app.post("/login")
def login(data: dict):
    res = requests.post(f"{USER_SERVICE}/login", json=data)
    return res.json()


# ---------- MOVIE ----------
@app.post("/add-movie")
def add_movie(data: dict):
    res = requests.post(f"{MOVIE_SERVICE}/add-movie", json=data)
    return res.json()


@app.get("/movies")
def get_movies():
    res = requests.get(f"{MOVIE_SERVICE}/movies")
    return res.json()


# ---------- BOOKING ----------
@app.post("/book")
def book(data: dict):
    res = requests.post(f"{BOOKING_SERVICE}/book", json=data)
    return res.json()


@app.get("/bookings")
def bookings():
    res = requests.get(f"{BOOKING_SERVICE}/bookings")
    return res.json()