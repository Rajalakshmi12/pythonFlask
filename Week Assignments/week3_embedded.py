from sentence_transformers import SentenceTransformer
import asyncio
import numpy as np
import httpx
import os

# Load local embedding model
model = SentenceTransformer('BAAI/bge-base-en-v1.5')  # A small, high-quality model

def embed_local(text: str) -> list[float]:
    return model.encode(text).tolist() # Get embedding vector for text using local model

def get_similarity(text1: str, text2: str) -> float:
    """Calculate cosine similarity between two texts."""
    emb1 = np.array(embed_local(text1))
    emb2 = np.array(embed_local(text2))
    return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

async def embed(text: str) -> list[float]:
    """Get embedding vector for text using OpenAI's API."""
    api_key = "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"  # Use environment variable for security

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://api.openai.com/v1/embeddings",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": "text-embedding-3-small",
                    "input": [
                        "Dear user, please verify your transaction code 59147 sent to 23ds3000149@ds.study.iitm.ac.in",
                        "Dear user, please verify your transaction code 96979 sent to 23ds3000149@ds.study.iitm.ac.in"
                        ]
                    }
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()["data"][0]["embedding"]
        except httpx.HTTPStatusError as e:
            print(f"HTTP error: {e.response.status_code} - {e.response.text}")
            return []
        except Exception as e:
            print(f"Request failed: {str(e)}")
            return []

async def main():
    print(await embed("Dear user, please verify your transaction code 59147 sent to 23ds3000149@ds.study.iitm.ac.in"))  # Fetch OpenAI embedding asynchronously
    print(await embed("Dear user, please verify your transaction code 96979 sent to 23ds3000149@ds.study.iitm.ac.in"))  # Fetch OpenAI embedding asynchronously

if __name__ == "__main__":
    asyncio.run(main())
