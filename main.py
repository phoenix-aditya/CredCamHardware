from image_capture import capture_image
from image_upload import upload_data_to_mongoDB, upload_image_to_ipfs

def click_image():
    img_path = capture_image()
    upload_data_to_mongoDB(
        image_path=img_path
        )

click_image()
