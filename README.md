# Flight Booking System

## Overview
This is a Python Tkinter-based flight booking system with SQLite backend.

## Setup
1. Install dependencies:
   ```
   pip install tkcalendar qrcode pillow
   ```

2. Run the app:
   ```
   python main.py
   ```

## Features
- Flight search by origin, destination
- Flight listing and booking UI
- Passenger details form and booking confirmation
- Admin panel for managing bookings
- QR code ticket generation and display

## Packaging
To create a standalone executable, use PyInstaller:

```bash
pyinstaller --onefile --windowed main.py --add-data "flights.db;." --add-data "qr_codes;qr_codes" --add-data "assets;assets"
```

Make sure to include the `resource_path` function in `database.py` to locate data files properly.

## Folder Structure
- `main.py` — Start UI
- `search_results.py` — Flight listings
- `booking_page.py` — Booking form
- `qr_ticket.py` — QR code generation
- `admin_panel.py` — Admin controls
- `database.py` — SQLite data handling
- `flights.db` — Database file
- `qr_codes/` — Generated QR codes
- `assets/` — Images and logos
