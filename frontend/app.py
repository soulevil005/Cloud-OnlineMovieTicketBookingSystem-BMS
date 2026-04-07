import streamlit as st
import requests

BASE_URL = "https://api-gateway-xxxx.onrender.com"  # 🔥 replace

st.set_page_config(page_title="BMS Flow App", layout="centered")

st.title("🎬 Movie Ticket Booking System")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- STEP 1: REGISTER ----------------
if st.session_state.step == 1:
    st.header("Step 1: Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password")

    if st.button("Register"):
        res = requests.post(f"{BASE_URL}/register", json={
            "name": name,
            "email": email,
            "password": password
        })

        st.write("Status:", res.status_code)
        st.write("Response:", res.text)

        if res.status_code == 200:
            st.success("Registered successfully")
            st.session_state.email = email
            st.session_state.step = 2

# ---------------- STEP 2: MOVIE ----------------
elif st.session_state.step == 2:
    st.header("Step 2: Select Movie")

    movie = st.text_input("Movie Name")
    genre = st.text_input("Genre")
    duration = st.number_input("Duration")

    if st.button("Add Movie"):
        res = requests.post(f"{BASE_URL}/add-movie", json={
            "name": movie,
            "genre": genre,
            "duration": int(duration)
        })

        if res.status_code == 200:
            st.success("Movie added")
            st.session_state.movie = movie
            st.session_state.step = 3

# ---------------- STEP 3: THEATRE ----------------
elif st.session_state.step == 3:
    st.header("Step 3: Select Theatre")

    theatre = st.text_input("Theatre Name")
    location = st.text_input("Location")

    if st.button("Add Theatre"):
        res = requests.post(f"{BASE_URL}/add-theatre", json={
            "name": theatre,
            "location": location,
            "movie_name": st.session_state.movie,
            "show_time": "7:00 PM"
        })

        if res.status_code == 200:
            st.success("Theatre added")
            st.session_state.step = 4

# ---------------- STEP 4: SEAT ----------------
elif st.session_state.step == 4:
    st.header("Step 4: Select Seats")

    seats = st.text_input("Seats (A1,A2)")

    if st.button("Lock Seats"):
        for seat in seats.split(","):
            requests.post(f"{BASE_URL}/lock-seat", params={
                "movie_name": st.session_state.movie,
                "seat_number": seat.strip()
            })

        st.success("Seats locked")
        st.session_state.seats = seats
        st.session_state.step = 5

# ---------------- STEP 5: PAYMENT ----------------
elif st.session_state.step == 5:
    st.header("Step 5: Payment")

    amount = st.number_input("Amount")

    if st.button("Pay"):
        res = requests.post(f"{BASE_URL}/pay", json={
            "user_email": st.session_state.email,
            "amount": amount
        })

        if res.status_code == 200:
            st.success("Payment successful")
            st.session_state.step = 6

# ---------------- STEP 6: BOOKING ----------------
elif st.session_state.step == 6:
    st.header("Step 6: Booking Confirmation")

    if st.button("Confirm Booking"):
        res = requests.post(f"{BASE_URL}/book", json={
            "user_email": st.session_state.email,
            "movie_name": st.session_state.movie,
            "seats": st.session_state.seats.split(",")
        })

        if res.status_code == 200:
            st.success("Booking Confirmed 🎉")

            # Notification
            requests.post(f"{BASE_URL}/notify", params={
                "user_email": st.session_state.email,
                "message": "Booking Confirmed"
            })

            st.success("Notification Sent 📩")