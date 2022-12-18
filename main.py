#!/usr/bin/env python

from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button, LED
import os
from signal import pause


def click_image():
    led.off()
    print('image capture begins')
    img_path = capture_image()
    print('image captured')
    print('uploading image to IPFS')
    print('uploaded image to IPFS')
    print('uploading metadata to MongoDB')
    upload_data_to_mongoDB(
        image_path=img_path
        )
    if os.path.exists("test.jpg"):
        os.remove("test.jpg")
    print('uploaded metadata to MongoDB')
    led.on()

# camera click button GPIO pin 22
os.system("/home/pi/CredCamHardware/intruder.py &")

button = Button(2)
led = LED(17)

led.on()
button.when_pressed = click_image
pause()
