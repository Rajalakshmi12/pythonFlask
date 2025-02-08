from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Query
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from typing import List
import numpy as np
import re
import json
import requests
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["OPTIONS", "POST"],
    allow_headers=["*"],
)

# Set your proxy API key
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZHMzMDAwMTQ5QGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.q_q9LIsqoM8So_zTtZkoHf_ppRlfrrzpzRenGNifW8k"

# Request payload model
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str
    
# Function to generate embeddings using proxy OpenAI
def get_embedding(text):
    url = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    json_data = {
        "model": "text-embedding-3-small",
        "input": text
    }
    
    response = requests.post(url=url, headers=headers, json=json_data)
    return response.json()['data'][0]['embedding']

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

@app.post("/similarity")
async def compute_similarity(request: SimilarityRequest):
    if not request.docs or not request.query:
        raise HTTPException(status_code=400, detail="Docs and query cannot be empty.")

    docs_input = request.docs
    query_input = request.query 

    # Generate embeddings for doc and query
    doc_embeddings = [get_embedding(doc) for doc in docs_input]
    query_embedding = get_embedding(query_input)
    
    # Compute similarity scores correctly as a **list**
    similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

    # Get top 3 most similar documents
    top_indices = np.argsort(similarities)[-3:][::-1]  # Get top 3 ranked indices
    top_matches = [docs_input[i] for i in top_indices]

    # Ensure response is always in compact format
    return ORJSONResponse({"matches": top_matches})

# Function to extract parameters and determine function mapping
def map_query_to_function(q: str):
    # Ticket status
    match = re.search(r"status of ticket (\d+)", q, re.IGNORECASE)
    if match:
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": int(match.group(1))})
        }
    
    # Meeting scheduling
    match = re.search(r"Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)", q, re.IGNORECASE)
    if match:
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            })
        }

    # Expense balance
    match = re.search(r"expense balance for employee (\d+)", q, re.IGNORECASE)
    if match:
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": int(match.group(1))})
        }

    # Performance bonus
    match = re.search(r"performance bonus for employee (\d+) for (\d{4})", q, re.IGNORECASE)
    if match:
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            })
        }

    # Office issue reporting
    match = re.search(r"office issue (\d+) for the (.+) department", q, re.IGNORECASE)
    if match:
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            })
        }

    return {"name": "unknown_function", "arguments": "{}"}

@app.get("/execute")
async def execute(q: str = Query(..., title="Query parameter")):
    result = map_query_to_function(q)
    return result
