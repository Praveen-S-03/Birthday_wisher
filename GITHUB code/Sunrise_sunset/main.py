import requests
import os
from dotenv import load_dotenv
load_dotenv()
# I have used my current coordinates if you want to find yours
# then replace my_lat and my_long to your coordinated and change the tzid to your timezome
api_endpoint = os.getenv("API_ENDPOINT")
my_lat = os.getenv("MY_LAT")
my_long =os.getenv("MY_LONG")
parameters ={
    "lat":my_lat,
    "lng":my_long,
    "tzid":"Asia/Kolkata"
}
response = requests.get(url=api_endpoint,params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]
print(f" The Sun will rise at {sunrise_time} and sets at {sunset_time}" )