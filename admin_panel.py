import tkinter as tk
from database import get_all_bookings

class AdminPanel:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Admin Panel")
        self.top.geometry("600x400")

        self.refresh_button = tk.Button(self.top, text="Refresh Bookings", command=self.load_bookings)
        self.refresh_button.pack(pady=5)

        self.bookings_list = tk.Listbox(self.top, width=80)
        self.bookings_list.pack(fill="both", expand=True)

        self.load_bookings()

    def load_bookings(self):
        self.bookings_list.delete(0, tk.END)
        bookings = get_all_bookings()
        for b in bookings:
            text = f"ID:{b['id']} Flight:{b['flight_no']} Name:{b['passenger_name']} Date:{b['travel_date']} Price:${b['price']}"
            self.bookings_list.insert(tk.END, text)
