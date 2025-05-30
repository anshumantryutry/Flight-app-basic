import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from database import save_booking
from qr_ticket import generate_qr

class BookingPage:
    def __init__(self, parent, flight):
        self.top = tk.Toplevel(parent)
        self.top.title(f"Book Flight {flight['flight_no']}")
        self.flight = flight

        tk.Label(self.top, text=f"Booking Flight {flight['flight_no']} from {flight['from_city']} to {flight['to_city']}").pack(pady=10)

        tk.Label(self.top, text="Passenger Name:").pack()
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack()

        tk.Label(self.top, text="Email:").pack()
        self.email_entry = tk.Entry(self.top)
        self.email_entry.pack()

        tk.Label(self.top, text="Phone:").pack()
        self.phone_entry = tk.Entry(self.top)
        self.phone_entry.pack()

        tk.Label(self.top, text="Passport Number:").pack()
        self.passport_entry = tk.Entry(self.top)
        self.passport_entry.pack()

        tk.Label(self.top, text="Travel Date:").pack()
        self.date_entry = DateEntry(self.top, width=12, background='darkblue',
                        foreground='white', borderwidth=2, year=2025)
        self.date_entry.pack(pady=5)

        tk.Button(self.top, text="Confirm Booking", command=self.book).pack(pady=15)

    def book(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        passport = self.passport_entry.get()
        travel_date = self.date_entry.get_date()

        if not (name and email and phone and passport):
            tk.messagebox.showerror("Error", "Please fill all fields")
            return

        booking_id = save_booking(
            self.flight["flight_no"], name, email, phone, passport, travel_date, self.flight["price"]
        )
        if booking_id:
            qr_path = generate_qr(booking_id)
            tk.messagebox.showinfo("Success", f"Booking confirmed! QR code saved at:{qr_path}")
            self.top.destroy()
        else:
            tk.messagebox.showerror("Error", "Booking failed. Try again.")
