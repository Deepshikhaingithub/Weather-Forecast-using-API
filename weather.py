import requests
import os
from datetime import datetime

api_address= 'https://api.openweathermap.org/data/2.5/weather?appid=a4adffc38a13763812d77192d3540ba6&q='
location= input("Enter your city name: ")

complete_api_link= api_address + location

api_data= requests.get(complete_api_link).json()
#print(api_data)

location_weather= api_data['weather'][0]['description']
location_temp= ((api_data['main']['temp'])- 273.15)
location_humidity= api_data['main']['humidity']
location_windspeed= api_data['wind']['speed']
date_time= datetime.now().strftime("%m/%d/%Y | %H:%M:%S")

if api_data['cod'] == '404':     
    print("Invalid city: {} , Please check your city name". format(location))
else:

    print("Weather Statistics for {} || {}" .format(location.upper(), date_time))
    print("Current weather description: ", location_weather)
    print("Current Temp : {:.2f} deg C". format(location_temp))
    print("Current Humidity :", location_humidity, "%")
    print("Current Wind Speed :", location_windspeed, "kmph")
