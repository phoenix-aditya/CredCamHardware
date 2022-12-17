import os

def capture_image() -> str:
    '''
    function takes an image in raspberry pi and returns the path to the image
    '''
    os.system("raspistill -o test.jpg")
    return "test.jpg"
