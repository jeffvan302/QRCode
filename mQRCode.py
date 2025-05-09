## pip install segno

# Testing Phase, not very useful since so little data can be stored in a micro QR code

import segno

data = ""

qrcode = segno.make(data)

print("Is Micro:", qrcode.is_micro)

qrcode.save("F:\OneDrive\OneDrive - Nardana Inc\Parkinson\QRt2.png")
