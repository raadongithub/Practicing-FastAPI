from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Ghar hu mai"}

@app.get("/about")
def about():
    return {"message": "Kya karu apni tareef mai?"}