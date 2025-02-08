import httpx
from geopy.geocoders import Nominatim
import time
from geopy.extra.rate_limiter import RateLimiter


# Public API that echoes responses

locator = Nominatim(user_agent='myGeocoder')
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

try:
    city = "Chennai"
    country = "India"
    location = geocode(f"{city},{country}")
    if location:
        #Fetch relevant details
        print(location.raw)   
        print(location.raw['boundingbox'])   
    
except Exception as e:
    print(f"Error: {e}")    



#print("Latitude {}, Longitude = {}".format(location.latitude, location.longitude))

def callWhenNeeded():
    URL = "https://postman-echo.com/get?response=Yes"
    try:
        response = httpx.get(URL)
        
        # Check if the response contains 'Yes'
        if response.status_code == 200 and response.json().get("args", {}).get("response") == "Yes":
            print(response.json()["args"]["response"])
        else:
            print("Unexpected Response:", response.text)

    except Exception as e:
        print("Error:", str(e))