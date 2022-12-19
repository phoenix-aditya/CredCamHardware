from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button, LED
import os
from signal import pause

intruder_light = LED(18)

intruder_light.off()
