from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

app = FastAPI()

@app.get("/status")
def test():
    return {"message": "up and running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
