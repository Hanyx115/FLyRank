from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
async def status():
    return {"status": "success", "code": 200}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)