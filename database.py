import sqlite3
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

DB_FILE = resource_path("flights.db")

def get_connection():
    return sqlite3.connect(DB_FILE)

def get_flights(from_city="", to_city=""):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM flights WHERE 1=1"
    params = []
    if from_city:
        query += " AND from_city LIKE ?"
        params.append('%' + from_city + '%')
    if to_city:
        query += " AND to_city LIKE ?"
        params.append('%' + to_city + '%')
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    flights = []
    for r in rows:
        flights.append({
            "flight_no": r[0],
            "from_city": r[1],
            "to_city": r[2],
            "departure_time": r[3],
            "price": r[4]
        })
    return flights

def save_booking(flight_no, passenger_name, email, phone, passport, travel_date, price):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO bookings (flight_no, passenger_name, email, phone, passport, travel_date, price) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (flight_no, passenger_name, email, phone, passport, travel_date, price))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(e)
        return None
    finally:
        conn.close()

def get_booking(booking_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings WHERE id=?", (booking_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    return {
        "id": row[0],
        "flight_no": row[1],
        "passenger_name": row[2],
        "email": row[3],
        "phone": row[4],
        "passport": row[5],
        "travel_date": row[6],
        "price": row[7]
    }

def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()
    bookings = []
    for r in rows:
        bookings.append({
            "id": r[0],
            "flight_no": r[1],
            "passenger_name": r[2],
            "email": r[3],
            "phone": r[4],
            "passport": r[5],
            "travel_date": r[6],
            "price": r[7]
        })
    return bookings
