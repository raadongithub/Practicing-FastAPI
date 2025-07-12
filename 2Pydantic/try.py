from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Dal diya')

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('badal rha hu bhai, sabar kr')


if __name__ == "__main__":
    while(True):
        name = input("nam bta!!!   ")
        age = int(input("Umar kya hh bhai teri?  "))

        choice = int(input("Ab ye bta Update(1) krna hh ya Insert(2)   "))
        patient_info = {'name': name, 'age':age}
        patient_obj = Patient(**patient_info)
        if choice == 1:
            update_patient(patient_obj)
        elif choice ==2:
            insert_patient(patient_obj)

        ex= input("Ab ye bta! or koi kam hh?(Y) ")
        if ex.lower() != 'y':
            print("Chal phir, mai ja rha")
            break

    
