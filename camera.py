# camera.py
from PIL import Image
from pyzbar.pyzbar import decode

# qr코드 리더
def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""