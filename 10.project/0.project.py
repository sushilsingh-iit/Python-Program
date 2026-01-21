#How to Create QR Code Generator in Python 

import qrcode as qr

#create qr code image

img = qr.make("sushil singh")

#save the image 

img.save("name_qr.png")
print("QR code saved as 'name_qr'")



