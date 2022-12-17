from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button, LED
import os
from signal import pause

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

# camera click button GPIO pin 22
button = Button(2)
led = LED(17)
led.on()
button.when_pressed = click_image
pause()

