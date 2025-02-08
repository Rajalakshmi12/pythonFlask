import httpx
import os

#Store a key in an environment variable
os.environ["API_KEY"] = "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"

# Retrieve the stored key
api_key = os.environ.get("API_KEY")

# url stores the OpenAI's API endpoint and dummy API key
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the request payload with two messages as mentioned in the activity
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "Analyze the sentiment of the given text & classify it as GOOD, BAD, or NEUTRAL !"},
        {"role": "user", "content": "q8Zl\nrnNGdi IXTIMdv Xd1 vP1 ZWF xMsEHp2LUiOAw7E1"}
    ]
}

def raise_for_status():
    print("Some exceptions")

try:
    # Send the request to OpenAI API
    response = httpx.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
    
    # Extract and print the response
    result = response.json()
    print(result)

except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
except httpx.RequestError as e:
    print(f"Request error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
