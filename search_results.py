import tkinter as tk
from booking_page import BookingPage

def show_search_results(parent, flights):
    results_win = tk.Toplevel(parent)
    results_win.title("Search Results")
    results_win.geometry("600x400")

    if not flights:
        tk.Label(results_win, text="No flights found.").pack(pady=20)
        return

    for flight in flights:
        text = f"Flight {flight['flight_no']}: {flight['from_city']} -> {flight['to_city']} "                f"Departure: {flight['departure_time']} Price: ${flight['price']}"
        btn = tk.Button(results_win, text=text,
                        command=lambda f=flight: BookingPage(results_win, f))
        btn.pack(pady=5)
