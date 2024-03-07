import requests
import json

city  = 'pune' #input("Enter the Name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=225b92fd7e1c481690670034231208&q={city}"

r = requests.get(url)

print(r.text)

wdic = json.loads(r.text)

print(wdic["location"]["name"])
print(wdic["current"]["temp_c"])