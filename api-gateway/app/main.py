from fastapi import FastAPI
import requests

app = FastAPI()

# ✅ DEPLOYED SERVICES
USER_SERVICE = "https://user-service-new-wzpd.onrender.com"
MOVIE_SERVICE = "https://movie-service-63iw.onrender.com"
BOOKING_SERVICE = "https://booking-service-ulkk.onrender.com"


@app.get("/")
def root():
    return {"message": "API Gateway Running"}


# 🔥 COMMON SAFE HANDLER
def safe_request(method, url, **kwargs):
    try:
        res = requests.request(method, url, timeout=10, **kwargs)

        # Try JSON first
        try:
            return res.json()
        except:
            return {
                "status_code": res.status_code,
                "response": res.text
            }

    except Exception as e:
        return {"error": str(e)}


# ---------- USER ----------
@app.post("/register")
def register(data: dict):
    return safe_request("POST", f"{USER_SERVICE}/register", json=data)


@app.post("/login")
def login(data: dict):
    return safe_request("POST", f"{USER_SERVICE}/login", json=data)


# ---------- MOVIE ----------
@app.post("/add-movie")
def add_movie(data: dict):
    return safe_request("POST", f"{MOVIE_SERVICE}/add-movie", json=data)


@app.get("/movies")
def get_movies():
    return safe_request("GET", f"{MOVIE_SERVICE}/movies")


# ---------- BOOKING ----------
@app.post("/book")
def book(data: dict):
    return safe_request("POST", f"{BOOKING_SERVICE}/book", json=data)


@app.get("/bookings")
def bookings():
    return safe_request("GET", f"{BOOKING_SERVICE}/bookings")