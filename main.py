# QR codes are used to encode and decode the data into a machine-readable form.
# The use of camera phones to read two-dimensional barcodes for
# various purposes is currently a popular topic in both types of research and practical applications.

# To generate QR Codes with Python you need to install only one Python library for this task pip install pyqrcode

import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
data = "https://github.com/"

# Generate QR code
url = pyqrcode.create(data)

# Create and save the png file naming "myqr.png"
url.svg("mygithub.svg", scale=8)