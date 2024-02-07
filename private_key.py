#! /usr/bin/python3
#charset: utf-8

import os
from Crypto.Hash import SHA256
import qrcode

def encryption(key, username):
    object_ = SHA256.new(key.encode('utf-8'))
    encrypt = object_.hexdigest()
    print(encrypt)
    qr = qrcode.QRCode(
         version=1,
         error_correction=qrcode.constants.ERROR_CORRECT_L,
         box_size=9,
         border=3,
    )
    qr.add_data(encrypt)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"static/{username}.png")
    return encrypt

    
