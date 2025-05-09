# pip install pylibdmtx

# Testing Phase: Promising since more of the space contains data.
# Flaws are that the distortion is not as well handled as the QR code.


from PIL import Image
from pylibdmtx.pylibdmtx import encode

data = ""

encoded = encode(data.encode("utf-8"))
img = Image.frombytes("RGB", (encoded.width, encoded.height), encoded.pixels)

img.save("F:\OneDrive\OneDrive - Nardana Inc\Parkinson\datamatrix.png")
img.show()


# print("Data Matrix barcode saved as datamatrix.png")
