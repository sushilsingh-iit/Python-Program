#How to Create QR Code Generator in Python 

import qrcode as qr

#create qr code image

img = qr.make("https://www.linkedin.com/in/sushilsingh-iit/?originalSubdomain=in")

#save the image 

img.save("profile_qr.png")
print("QR code saved as 'profile_qr'")



