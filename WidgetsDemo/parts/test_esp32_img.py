import binascii
import datetime
from io import BytesIO
from PIL import Image
import requests


def begin_url(url):
    response = requests.get(url + 'HandleVal?ssid=snapshot&password=daodanjishui')
    if response.status_code == 200:
        binary_data = binascii.unhexlify(response.text)
        image = Image.open(BytesIO(binary_data))
        image.save(f'img{datetime.datetime.now().strftime(" %H-%M-%S")}.jpg')
        image.show()


if __name__ == '__main__':
    esp32cam_url = 'http://192.168.4.1/'
    begin_url(esp32cam_url)
