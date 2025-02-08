import requests

response = requests.get("https://www.thesaranshsaini.com/api/projectsFetcher")
print(response.json())  # Check if it works
#Checking