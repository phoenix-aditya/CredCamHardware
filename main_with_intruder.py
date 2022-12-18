#!/usr/bin/env python

from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button, LED
import os
from signal import pause

button = Button(2)
led = LED(17)
intruder_light = LED(18)
detector1 = Button(4)
detector2 = Button(26)
detector3 = Button(20)
detector4 = Button(18)

def click_image():
    led.off()
    print('image capture begins')
    img_path = capture_image()
    upload_data_to_mongoDB(
        image_path=img_path
        )
    if os.path.exists("test.jpg"):
        os.remove("test.jpg")
    print('image capture ends')
    led.on()

def intruder_detected():
    intruder_light.on()

# camera click button GPIO pin 22


led.on()

while True:
    if button.is_pressed:
        click_image()
        pause()

    if detector1.is_pressed:
        intruder_detected()
    if detector2.is_pressed():
        intruder_detected()
    if detector3.is_pressed():
        intruder_detected()
    if detector4.is_pressed():
        intruder_detected()

# button.when_pressed = click_image
# pause()

