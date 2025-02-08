import requests
import numpy as np
import httpx

# Set your proxy API key
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMTQ5QGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.q_q9LIsqoM8So_zTtZkoHf_ppRlfrrzpzRenGNifW8k"

url="http://aiproxy.sanand.workers.dev/openai/v1/embeddings"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

json_data_b = {
    "model": "text-embedding-3-small",
    "input": "Bicycle"
}

json_data_c = {
    "model": "text-embedding-3-small",
    "input": "Cycle"
}

response = requests.post(url=url, headers=headers, json = json_data_b)
process_bicycle = response.json()['data'][0]['embedding']

response = requests.post(url=url, headers=headers, json = json_data_c)
process_cycle = response.json()['data'][0]['embedding']

cosine_similarity = np.dot(process_bicycle,process_cycle)
print(cosine_similarity)

similarities = cosine_similarity(process_bicycle, process_cycle)
print(similarities)


# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2)