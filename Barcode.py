# pip install python-barcode Pillow

# Testing Phase

import barcode
from barcode.writer import ImageWriter

barcode_data = ""
ENGine = barcode.get_barcode_class("code128")
output = ENGine(barcode_data, writer=ImageWriter())

filename = output.save("barcode")
