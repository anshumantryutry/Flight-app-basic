import tkinter as tk
from database import get_flights
from search_results import show_search_results
from booking_page import BookingPage
from admin_panel import AdminPanel

def main():
    root = tk.Tk()
    root.title("Flight Booking System")
    root.geometry("800x600")

    tk.Label(root, text="Welcome to Flight Booking System", font=("Arial", 18)).pack(pady=20)

    # Simple search form
    from_city = tk.StringVar()
    to_city = tk.StringVar()

    tk.Label(root, text="From:").pack()
    from_entry = tk.Entry(root, textvariable=from_city)
    from_entry.pack()

    tk.Label(root, text="To:").pack()
    to_entry = tk.Entry(root, textvariable=to_city)
    to_entry.pack()

    def search():
        flights = get_flights(from_city.get(), to_city.get())
        show_search_results(root, flights)

    tk.Button(root, text="Search Flights", command=search).pack(pady=10)

    # Admin panel button
    tk.Button(root, text="Admin Panel", command=lambda: AdminPanel(root)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
