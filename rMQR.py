# pip install rmqrcode

# Testing Phase: Not very useful since phones don't read these codes

import rmqrcode
from rmqrcode import QRImage, rMQR

data = ""

qr = rMQR.fit(
    data,
    ecc=rmqrcode.ErrorCorrectionLevel.M,
    fit_strategy=rmqrcode.FitStrategy.MINIMIZE_WIDTH,
)


image = QRImage(qr, module_size=8)
image.show()
