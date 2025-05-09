# pip install qrcode

# qrcode library details:
# https://github.com/lincolnloop/python-qrcode


import qrcode

data = ""

# build up data lines if you want this all in one QR code
data += "Data Line 1\n"
data += "Data Line 2\n"
data += "Data Line 3\n"
data += "Data Line 4\n"


# or assign a single line of a url
data = ""

print("QR Code Generator\n")

print("QR Code Size is determined by the version of code.")
print("The higher the version, the more data it can hold.")
print(
    "Version 1 = 21x21 matrix, Version 2 = 25x25 matrix, Version 3 = 29x29 matrix, etc."
)
print(
    "The generator will automatically choose higher versions if the current version isn't big enough."
)

print("\n")

level_of_error_correction = 0
# 0 = low, 1 = medium, 2 = high, 3 = very high
# 0 = 7% of image can be damaged
# 1 = 15% of image can be damaged
# 2 = 25% of image can be damaged
# 3 = 30% of image can be damaged


print(
    "QR Border Size\n  The border is the number of boxes (pixels) to use for the border.\n  The default is 4, which results in a wide enough border for seperation.\n  You could go very small to 1 or 0 and still get good results.\n  It depends on your application."
)
border_size_i = input("Enter border size (default 4): ")
try:
    border_size = int(border_size_i)
except ValueError:
    print("Invalid input. Using default border size (4).")
    border_size = 4

print(
    "QR Icons\n  If you want to place a small icon in the center of the QR code then,\n  use a higher level of error correction.\n  This will give you redundancy in the QR code.\n  Allowing the center to be 'destroyed'."
)
print("QR Code can have a level of error correction.")
print("0 = L, 1 = M, 2 = Q, 3 = H")
print("0 = 7% of image can be damaged")
print("1 = 15% of image can be damaged")
print("2 = 25% of image can be damaged")
print("3 = 30% of image can be damaged")


error_l = input("Enter level of error correction (0-3): ")
try:
    level_of_error_correction = int(error_l)
except ValueError:
    print("Invalid input. Using default level of error correction (1).")
    level_of_error_correction = 1

print(
    "Specify the data to encode in the QR code.\n  If it is a URL then hit enter on the next line to have a single data line."
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


error_correction_v = qrcode.constants.ERROR_CORRECT_M

if level_of_error_correction == 0:
    # low error correction
    error_correction_v = qrcode.constants.ERROR_CORRECT_L
elif level_of_error_correction == 1:
    # medium error correction
    error_correction_v = qrcode.constants.ERROR_CORRECT_M
elif level_of_error_correction == 2:
    # high error correction
    error_correction_v = qrcode.constants.ERROR_CORRECT_Q
elif level_of_error_correction == 3:
    # very high error correction
    error_correction_v = qrcode.constants.ERROR_CORRECT_H


# QR Code Version List: https://www.qrcode.com/en/about/version.html
# The higher the version, the more data it can hold.
# Version 1 = 21x21 matrix, Version 2 = 25x25 matrix, Version 3 = 29x29 matrix, etc.
# The generator will automatically choose higher versions if the current version isn't big enough.

# The box_size is the pixel size of each box in the QR code.
# The border is the number of boxes to use for the border. The default is 4, which is the minimum.


qr = qrcode.QRCode(
    version=1,
    error_correction=error_correction_v,
    box_size=5,
    border=border_size,
)


qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
# see which version was used to encode the data
# can use this to determine if the QR code is too large for the engraver.
# if you know the most you can engrave is version 3 at level of error correction 3 then version 4 would not work here.
print("Version: ", qr.version)

filename = input('Enter filename to save QR code (default "QR code"): ')
if filename == "":
    filename = "QR code"

filename += ".png"

img.save(filename)

img.show()
