import requests
api_endpoint = "http://api.open-notify.org/iss-now.json"
#The above link is used to find the position of IIS
response = requests.get(url=api_endpoint)
response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
print(f"The International Space station is at {latitude} Latitude and {longitude} Longitude")
