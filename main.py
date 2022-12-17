from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs
from gpiozero import Button
import os

def click_image():
    img_path = capture_image()
    upload_data_to_mongoDB(
        image_path=img_path
        )
    if os.path.exists("test.jpg"):
        os.remove("test.jpg")

# camera click button GPIO pin 22
button = Button(22)

button.wait_for_press()
print('button pressed')

# while True:
#     if button.is_pressed:
#         print("Button is pressed")
#         # click_image()
#         print("image upload complete")


