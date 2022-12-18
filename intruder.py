#!/usr/bin/env python

from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button, LED
import os
from signal import pause

intruder_light = LED(18)
detector1 = Button(4)
detector2 = Button(26)
detector3 = Button(20)
detector4 = Button(16)

def intruder_detected():
    intruder_light.on()

# camera click button GPIO pin 22

while True:
    if detector1.is_pressed:
        intruder_detected()
    if detector2.is_pressed:
        intruder_detected()
    if detector3.is_pressed:
        intruder_detected()
    if detector4.is_pressed:
        intruder_detected()

intruder_light.off()

