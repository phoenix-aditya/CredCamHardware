import os

def capture_image() -> str:
    '''
    function takes an image in raspberry pi and returns the path to the image
    '''
    os.system("raspistill -o /home/pi/CredCamHardware/test.jpg")
    return "/home/pi/CredCamHardware/test.jpg"
