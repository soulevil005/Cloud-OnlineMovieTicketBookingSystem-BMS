from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE = "https://user-service-pcyb.onrender.com"
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
            "gateway_status": "ok",
            "service_status": response.status_code,
            "service_response": response.text
        }
    except Exception as e:
        return {"error": str(e)}

# ---------- MOVIE ----------
@app.post("/add-movie")
def add_movie(data: dict):
    response = requests.post(f"{MOVIE_SERVICE}/add-movie", json=data)
    return response.json()


@app.get("/movies")
def get_movies():
    response = requests.get(f"{MOVIE_SERVICE}/movies")
    return response.json()


# ---------- BOOKING ----------
@app.post("/book")
def book(data: dict):
    response = requests.post(f"{BOOKING_SERVICE}/book", json=data)
    return response.json()


@app.get("/bookings")
def bookings():
    response = requests.get(f"{BOOKING_SERVICE}/bookings")
    return response.json()


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