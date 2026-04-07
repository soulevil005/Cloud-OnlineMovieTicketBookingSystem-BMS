import streamlit as st
import requests

BASE_URL = "https://api-gateway-g5wc.onrender.com"  

st.set_page_config(page_title="BMS App", layout="wide")

st.title("🎬 Movie Ticket Booking System")

menu = st.sidebar.radio("Menu", [
    "Register",
    "Add Movie",
    "View Movies",
    "Book Ticket",
    "View Bookings"
])

# ---------- REGISTER ----------
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
        st.write(res.json())


# ---------- ADD MOVIE ----------
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
        st.write(res.json())


# ---------- VIEW MOVIES ----------
elif menu == "View Movies":
    st.header("Movies")

    if st.button("Load"):
        res = requests.get(f"{BASE_URL}/movies")
        st.write(res.json())


# ---------- BOOK ----------
elif menu == "Book Ticket":
    st.header("Book Ticket")

    email = st.text_input("Email")
    movie = st.text_input("Movie Name")
    seats = st.text_input("Seats")

    if st.button("Book"):
        res = requests.post(f"{BASE_URL}/book", json={
            "user_email": email,
            "movie_name": movie,
            "seats": seats.split(",")
        })
        st.write(res.json())


# ---------- BOOKINGS ----------
elif menu == "View Bookings":
    st.header("Bookings")

    if st.button("Load"):
        res = requests.get(f"{BASE_URL}/bookings")
        st.write(res.json())