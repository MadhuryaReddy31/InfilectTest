from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

app = FastAPI()

@app.post("/shelf_identification")
def shelf_identification(input_data:list[list[str]]):
    layout = input_data
    result = {}

    for row in layout:
        for c in set(row):

            occupied_rows = []
            occupied_cols = []
        
            for i, r in enumerate(layout):
                for j, val in enumerate(r):
                    if val == c:
                        occupied_rows.append(i)
                        occupied_cols.append(j)
                
            if len(set(occupied_cols)) == 1:
                if min(occupied_cols) == 0:
                    location = ["left"]
                else:
                    location = ["right"]
                
            elif len(set(occupied_rows)) == 1:
                location = ["horizontal"]
                
            elif 0 in occupied_rows and 0 in occupied_cols:
                location = ["top left"]
            
            elif 0 in occupied_rows and len(row)-1 in occupied_cols:
                location = ["top right"]  
                
            elif len(layout)-1 in occupied_rows and 0 in occupied_cols:
                location = ["bottom left"]   
                
            elif len(layout)-1 in occupied_rows and len(row)-1 in occupied_cols:
                location = ["bottom right"]
                
            else:
                location = ["middle"]
                
             
            min_row = min(occupied_rows)
            max_row = max(occupied_rows)
            min_col = min(occupied_cols)
            max_col = max(occupied_cols)
            
            height = max_row - min_row + 1
            width = max_col - min_col + 1
            
            if height == 1:
                shape = "horizontal rectangle"
                
            elif width == 1:
                shape = "vertical rectangle"
                
            elif height == width:
                shape = "square"
                
            else:
                shape = "polygon"

            result[c] = {"shape": shape, "location": location}

    return result


@app.get("/status")
def test():
    return {"message": "up and running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
