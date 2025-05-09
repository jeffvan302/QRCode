# QRCode

The QRcode.py is the main script for creating QR Codes.  

It does require the qrcode library that can be installed with the command below

```
pip install qrcode
```

Running the QRCode.py will step you through creating a QRCode and what you need to know for the basic creation of the Image.

The other scripts are work in progress and in general are not very useful.

The best next thing to QRCodes is the DataMatrix.py 
DataMatrix is a lot more dense for information storage in the image than QRCodes.
But it comes with drawbacks.  The latest version of QRCodes has distortion correction and a heavier error correction for damaged images.

DataMatrix are more restricted in the manner, but because of its higher data density can be useful if you need to squeeze that last bit of information into a smaller image area.

