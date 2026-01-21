#How to Create QR Code Generator in Python 
# modified qr code create 

import qrcode
from PIL import Image


# You can usually access constants directly from the module if imported,
# or via qrcode.constants.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # UPDATED
    box_size=10,
    border=4,
)

qr.add_data("https://www.linkedin.com/in/sushilsingh-iit/?originalSubdomain=in")
qr.make(fit=True) 

img = qr.make_image(fill_color="red", back_color="black")
img.save("profile.png")

print("qr saved as png file 'profile.png'")