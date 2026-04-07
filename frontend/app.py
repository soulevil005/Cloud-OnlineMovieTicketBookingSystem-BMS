import streamlit as st
import requests

BASE_URL = "https://api-gateway-g5wc.onrender.com"

st.set_page_config(page_title="BMS App", layout="wide")

st.title("🎬 Movie Ticket Booking System")

# 🔥 COMMON RESPONSE HANDLER
def display_response(res):
    try:
        data = res.json()
        st.success("✅ Success")
        st.json(data)
    except:
        if res.text.strip() == "":
            st.warning("⚠️ Empty response from server")
        else:
            st.error("⚠️ Non-JSON response")
            st.code(res.text)


menu = st.sidebar.radio("Menu", [
    "Register",
    "Add Movie",
    "View Movies",
    "Book Ticket",
    "View Bookings"
])

# ---------- REGISTER ----------
if menu == "Register":
    st.header("👤 Register User")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.warning("Please fill all fields")
        else:
            with st.spinner("Registering..."):
                res = requests.post(f"{BASE_URL}/register", json={
                    "name": name,
                    "email": email,
                    "password": password
                })
                display_response(res)


# ---------- ADD MOVIE ----------
elif menu == "Add Movie":
    st.header("🎬 Add Movie")

    movie = st.text_input("Movie Name")
    genre = st.text_input("Genre")
    duration = st.number_input("Duration", min_value=1)

    if st.button("Add Movie"):
        if not movie or not genre:
            st.warning("Please fill all fields")
        else:
            with st.spinner("Adding movie..."):
                res = requests.post(f"{BASE_URL}/add-movie", json={
                    "name": movie,
                    "genre": genre,
                    "duration": int(duration)
                })
                display_response(res)


# ---------- VIEW MOVIES ----------
elif menu == "View Movies":
    st.header("📖 Movies")

    if st.button("Load Movies"):
        with st.spinner("Fetching movies..."):
            res = requests.get(f"{BASE_URL}/movies")
            display_response(res)


# ---------- BOOK ----------
elif menu == "Book Ticket":
    st.header("🎟 Book Ticket")

    email = st.text_input("User Email")
    movie = st.text_input("Movie Name")
    seats = st.text_input("Seats (A1,A2)")

    if st.button("Book Ticket"):
        if not email or not movie or not seats:
            st.warning("Please fill all fields")
        else:
            with st.spinner("Booking tickets..."):
                res = requests.post(f"{BASE_URL}/book", json={
                    "user_email": email,
                    "movie_name": movie,
                    "seats": [s.strip() for s in seats.split(",")]
                })
                display_response(res)


# ---------- BOOKINGS ----------
elif menu == "View Bookings":
    st.header("📊 Bookings")

    if st.button("Load Bookings"):
        with st.spinner("Fetching bookings..."):
            res = requests.get(f"{BASE_URL}/bookings")
            display_response(res)