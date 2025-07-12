from fastapi import FastAPI
import json 


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/")
def home():
    return {"message": "Ghar hu mai"}

@app.get("/about")
def about():
    return {"message": "Kya karu apni tareef mai?"}


@app.get("/view")
def view():
    data = load_data()
    return data