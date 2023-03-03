import requests

api_key = "92726743c1b91f71118b3a74e931ac01"
city = "Orlando"
url = "http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=5&appid="+api_key

requests = requests.get(url)
json = requests.json()
print(json)