from fastapi import FastAPI, Path, HTTPException, Query

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


@app.get("/view/{patient_id}")
def view(patient_id:str=Path(..., description="Patient ID to view details", example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Ye bnda abi mareez nai bna")


@app.get("/sort/")
def sort_patients(sort_by:str=Query(..., description='Height, Weight, BMI'), order:str=Query('asc', description="'asc'ending order or 'desc'ending order")):
    
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        HTTPException(status_code=400, detail='Sahi Field Choose kr ustad')

    if order not in ['asc', 'dsc']:
        HTTPException(status_code=400, detail='Sahi order Choose kr ustaddd')

    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_date = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_date
    