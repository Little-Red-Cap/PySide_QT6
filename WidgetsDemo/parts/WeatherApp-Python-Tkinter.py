import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = '7dad7462bab24329ba6bf1c81aee4971'  # 用您自己的Weatherbit API密钥替换


# 获取天气数据
def get_weather_data(city_name):
    url = f"https://api.weatherbit.io/v2.0/current"
    params = {
        "city": city_name,
        "key": API_KEY,
        "units": "I"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


# 显示天气信息
def display_weather(data):
    # print(data)
    if data:
        weather_data = data["data"][0]
        weather_info.set(f"Weather in {weather_data['city_name']}, {weather_data['country_code']}:\n"
                         f"Temperature: {weather_data['temp']}°F\n"
                         f"Description: {weather_data['weather']['description']}\n"
                         f"Humidity: {weather_data['rh']}%\n"
                         f"Wind Speed: {weather_data['wind_spd']} m/s")
    else:
        weather_info.set("Error fetching weather data.")


'''
{'count': 1, 'data': [{'app_temp': 71.9, 'aqi': 244, 'city_name': 'Beijing', 'clouds': 86, 'country_code': 'CN', 'datetime': '2024-06-10:16', 'dewpt': 62.3, 'dhi': 0, 'dni': 0, 'elev_angle': -26.78, 'ghi': 0, 'gust': None, 'h_angle': -90, 'lat': 39.9075, 'lon': 116.39723, 'ob_time': '2024-06-10 16:03', 'pod': 'n', 'precip': 0, 'pres': 997.5, 'rh': 73, 'slp': 1001, 'snow': 0, 'solar_rad': 0, 'sources': ['ZBAA', 'radar', 'satellite'], 'state_code': '22', 'station': 'ZBAA', 'sunrise': '20:43', 'sunset': '11:43', 'temp': 71.6, 'timezone': 'Asia/Shanghai', 'ts': 1718035437, 'uv': 0, 'vis': 9.9, 'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03n'}, 'wind_cdir': 'N', 'wind_cdir_full': 'north', 'wind_dir': 0, 'wind_spd': 2.2}]}
'''
received_data = {
    'count': 1,
    'data': [{
        'app_temp': 71.9,
        'aqi': 244,
        'city_name': 'Beijing',
        'clouds': 86,
        'country_code': 'CN',
        'datetime': '2024-06-10:16',
        'dewpt': 62.3,
        'dhi': 0,
        'dni': 0,
        'elev_angle': -26.78,
        'ghi': 0,
        'gust': None,
        'h_angle': -90,
        'lat': 39.9075,
        'lon': 116.39723,
        'ob_time': '2024-06-10 16:03',
        'pod': 'n',
        'precip': 0,
        'pres': 997.5,
        'rh': 73,
        'slp': 1001,
        'snow': 0,
        'solar_rad': 0,
        'sources': ['ZBAA', 'radar', 'satellite'],
        'state_code': '22',
        'station': 'ZBAA',
        'sunrise': '20:43',
        'sunset': '11:43',
        'temp': 71.6,
        'timezone': 'Asia/Shanghai',
        'ts': 1718035437,
        'uv': 0,
        'vis': 9.9,
        'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03n'},
        'wind_cdir': 'N',
        'wind_cdir_full': 'north',
        'wind_dir': 0,
        'wind_spd': 2.2}]
}


# 获取天气按钮的点击事件
def get_weather():
    city = city_entry.get()
    weather_data = get_weather_data(city)
    display_weather(weather_data)


# 创建主GUI窗口
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  # 设置窗口的初始大小

# 创建和配置GUI元素
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12, "bold"))
get_button.pack()

weather_info = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_info, font=("Helvetica", 12), justify="left")
weather_label.pack(pady=10)

# 启动GUI事件循环
root.mainloop()
