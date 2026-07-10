from fastapi import FastAPI
import uvicorn
from repository import PostgresRepo 
# from repository import InMemoryRepo  <-- The old way

app = FastAPI()

# THE SWAP: We changed one line of code here.
repo = PostgresRepo() 

@app.get("/items")
def read_items():
    return repo.get_items()

@app.post("/items")
def create_item(name: str, description: str):
    return repo.create_item(name, description)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)