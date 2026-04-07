from fastapi import FastAPI
import requests

app = FastAPI()

# Service URLs
USER_SERVICE = "https://user-service-pcyb.onrender.com/"
MOVIE_SERVICE = "https://movie-service-63iw.onrender.com"
BOOKING_SERVICE = "https://booking-service-ulkk.onrender.com"
SEAT_SERVICE = "http://127.0.0.1:8003"
PAYMENT_SERVICE = "http://127.0.0.1:8004"
THEATRE_SERVICE = "http://127.0.0.1:8005"
NOTIFICATION_SERVICE = "http://127.0.0.1:8006"


@app.get("/")
def root():
    return {"message": "API Gateway Running"}

# ---------- USER ----------
@app.post("/register")
def register(data: dict):
    try:
        response = requests.post(f"{USER_SERVICE}/register", json=data)
        return {
            "status_code": response.status_code,
            "response": response.text
        }
    except Exception as e:
        return {"error": str(e)}
@app.post("/login")
def login(data: dict):
    return requests.post(f"{USER_SERVICE}/login", json=data).json()

# ---------- MOVIES ----------
@app.get("/movies")
def get_movies():
    return requests.get(f"{MOVIE_SERVICE}/movies").json()

@app.post("/add-movie")
def add_movie(data: dict):
    return requests.post(f"{MOVIE_SERVICE}/add-movie", json=data).json()

# THEATRE
@app.post("/add-theatre")
def add_theatre(data: dict):
    return requests.post(f"{THEATRE_SERVICE}/add-theatre", json=data).json()

@app.get("/theatres")
def get_theatres():
    return requests.get(f"{THEATRE_SERVICE}/theatres").json()

# ---------- BOOKING ----------
@app.post("/book")
def book(data: dict):
    return requests.post(f"{BOOKING_SERVICE}/book", json=data).json()

@app.get("/bookings")
def bookings():
    return requests.get(f"{BOOKING_SERVICE}/bookings").json()

# ---------- SEAT ----------
@app.post("/lock-seat")
def lock_seat(movie_name: str, seat_number: str):
    return requests.post(
        f"{SEAT_SERVICE}/lock-seat",
        params={"movie_name": movie_name, "seat_number": seat_number}
    ).json()

@app.get("/seats")
def seats():
    return requests.get(f"{SEAT_SERVICE}/seats").json()

# ---------- PAYMENT ----------
@app.post("/pay")
def pay(data: dict):
    return requests.post(f"{PAYMENT_SERVICE}/pay", json=data).json()

# NOTIFICATION
@app.post("/notify")
def notify(user_email: str, message: str):
    return requests.post(
        f"{NOTIFICATION_SERVICE}/notify",
        params={"user_email": user_email, "message": message}
    ).json()