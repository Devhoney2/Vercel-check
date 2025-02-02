from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the data
data = pd.read_csv('api/q-vercel-python.json')

@app.get("/api")
async def get_marks(name: list):
    result = data[data['name'].isin(name)]['marks'].tolist()
    return {"marks": result}
