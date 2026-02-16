from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/")
def root():
    return {"message": "Simple Python Microservice"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/count")
def get_count():
    return {"counter": counter}

@app.post("/count")
def increment():
    global counter
    counter += 1
    return {"counter": counter}
