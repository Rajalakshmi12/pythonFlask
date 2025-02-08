from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS (Allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

# Load student data from CSV (assuming 'students.csv' exists in the same directory)
df = pd.read_csv("students.csv")  # Ensure the CSV file is present

@app.get("/api")
async def get_students(class_: list[str] = Query(None, alias="class")):
    """
    API endpoint to get students.
    - If no 'class' filter is provided, return all students.
    - If class filters are provided, return only students matching those classes.
    """
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    return {"students": filtered_df.to_dict(orient="records")}

# Run the server using:
# uvicorn server:app --host 127.0.0.1 --port 8000
