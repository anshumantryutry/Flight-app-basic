import qrcode
import os

QR_FOLDER = "qr_codes"

def generate_qr(booking_id):
    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)
    data = f"Booking ID: {booking_id}"
    img = qrcode.make(data)
    path = os.path.join(QR_FOLDER, f"booking_{booking_id}.png")
    img.save(path)
    return path
