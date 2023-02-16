import requests

API_KEY = "Add_yuour_own_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"  #f string is use to add variable and constants at same time
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] - 273.15,2)

    print("Weather: ", weather)
    print("Temperatute: ", temp, "celsius")
else:
    print("An error occured")    
