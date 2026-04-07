import streamlit as st
import requests

BASE_URL = "https://api-gateway-xxxx.onrender.com"  # 🔥 REPLACE WITH YOUR GATEWAY

st.set_page_config(page_title="BMS Cloud App", layout="wide")

st.title("🎬 Cloud Movie Ticket Booking System")

menu = st.sidebar.selectbox("Menu", ["Register", "Add Movie", "Book Ticket", "View Bookings"])

# ---------------- REGISTER ----------------
if menu == "Register":
    st.header("Register User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password")

    if st.button("Register"):
        res = requests.post(f"{BASE_URL}/register", json={
            "name": name,
            "email": email,
            "password": password
        })
        st.success(res.text)

# ---------------- ADD MOVIE ----------------
elif menu == "Add Movie":
    st.header("Add Movie")
    movie = st.text_input("Movie Name")
    genre = st.text_input("Genre")
    duration = st.number_input("Duration")

    if st.button("Add Movie"):
        res = requests.post(f"{BASE_URL}/add-movie", json={
            "name": movie,
            "genre": genre,
            "duration": int(duration)
        })
        st.success(res.text)

# ---------------- BOOK ----------------
elif menu == "Book Ticket":
    st.header("Book Ticket")
    email = st.text_input("User Email")
    movie = st.text_input("Movie Name")
    seats = st.text_input("Seats (A1,A2)")

    if st.button("Book"):
        res = requests.post(f"{BASE_URL}/book", json={
            "user_email": email,
            "movie_name": movie,
            "seats": seats.split(",")
        })
        st.success(res.text)

# ---------------- VIEW BOOKINGS ----------------
elif menu == "View Bookings":
    st.header("Bookings")

    if st.button("Load"):
        res = requests.get(f"{BASE_URL}/bookings")
        st.json(res.json())