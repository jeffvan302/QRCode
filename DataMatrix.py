# pip install pylibdmtx

# Promising since more of the space contains data.
# Flaws are that the distortion is not as well handled as the QR code.


from PIL import Image
from pylibdmtx.pylibdmtx import encode

print("QR Code Generator\n")

data = ""


print(
    "Specify the data to encode in the Data Matrix.\n  If it is a URL then hit enter on the next line to have a single data line."
)
i_num_lines = input("Enter number of lines (default single line): ")

try:
    num_lines = int(i_num_lines)
except ValueError:
    num_lines = 1

if num_lines < 1:
    num_lines = 1

for i in range(num_lines):
    data += input(f"Enter line {i+1} of data: ")
    if i < num_lines - 1:
        data += "\n"

print("Data: ", data)

encoded = encode(data.encode("utf-8"))

img = Image.frombytes("RGB", (encoded.width, encoded.height), encoded.pixels)


filename = input('Enter filename to save QR code (default "datamatrix"): ')
if filename == "":
    filename = "datamatrix"

filename += ".png"

img.save(filename)
img.show()
