import requests

city = input("What city would you like the weather for?\n")
url = 'http://api.weatherapi.com/v1/current.json?key=8107c044436a4e94bdd213631230704&q='+city+'&aqi=no'

try:
    response = requests.get(url)
    weather_json = response.json()

    temp = weather_json.get('current').get('temp_f')
    description = weather_json.get('current').get('condition').get('text')
    print("Today's weather in", city, "is", description, "and", int(temp), "degrees")
except AttributeError:
    print("You must enter a valid city")