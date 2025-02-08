
import requests
import json

# OpenAI tokenizer API URL (this might require specific endpoints)
url = "https://api.openai.com/v1/tokenizer"

# Your OpenAI API Key
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMTQ5QGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.q_q9LIsqoM8So_zTtZkoHf_ppRlfrrzpzRenGNifW8k"

# Text to tokenize
text = "Hello, how many tokens will this text use?"

# Define the request payload
data = {
    "text": text
}

# Headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Send the request
try:
    response = requests.post(url, json=data, headers=headers)
    if "application/json" in response.headers.get("Content-Type", ""):
        print(response.json())
    else:
        data=response.text
        print(data)
    
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON. Raw response:")
    print(response.text)

