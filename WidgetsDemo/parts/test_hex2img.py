import binascii
from io import BytesIO
from PIL import Image
import requests


def hex2img(hex_data_filepath):
    if hex_data_filepath.split('.')[-1] == 'txt':
        with open(hex_data_filepath, 'r') as f:  # 从文件中读取十六进制数据
            hex_data = f.read().strip()
        binary_data = binascii.unhexlify(hex_data)  # 将十六进制字符串转换为字节数组
        image = Image.open(BytesIO(binary_data))    # 将字节数组解码为图像
        # image.save(img_name.replace('.txt', '.jpg'))  # 保存图像
        # print(img_name.replace('.txt', '.jpg'))
        image.show()    # 显示图像


def download_img(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def begin_url(url):
    # 发送命令
    command = {'ssid': 'snapshot', 'password': 'daodanjishui'}
    # response = requests.post(url + 'HandleVal', data=command)
    # response = requests.get('http://192.168.4.1/HandleVal?ssid=snapshot&password=daodanjishui')
    response = requests.get(url + 'HandleVal?ssid=snapshot&password=daodanjishui')
    # 打印响应
    print(response.text)
    binary_data = binascii.unhexlify(response.text)  # 将十六进制字符串转换为字节数组
    image = Image.open(BytesIO(binary_data))    # 将字节数组解码为图像
    image.show()  # 显示图像


if __name__ == '__main__':
    # img_name = 'img1.txt'
    # hex2img(img_name)
    esp32cam_url = 'http://192.168.4.1/'
    begin_url(esp32cam_url)
