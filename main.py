from fastapi import FastAPI
from models import System, Student, Booking
from database import create_db_and_tables, get_db

app = FastAPI(title="Lab System Tracker") 

@app.get('/')
def home():
    return {"message": "Server is running"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

from sqlmodel import Session, select
from fastapi import Depends, HTTPException


@app.post("/systems/", response_model=System, status_code=201)
def create_system(system: System, db: Session = Depends(get_db)):
    db.add(system)
    db.commit()
    db.refresh(system)
    return system

@app.post("/students/", response_model=Student, status_code=201)
def create_student(student: Student, db: Session = Depends(get_db)):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

from typing import List

# List means type hinting, that, the OUTPUT response model should be a LIST of elements with type `System`. Much like generics in java.

# List of System class types [1,2,3] [System class, System class] => different class values

@app.get("/systems/", response_model=List[System], status_code=200)
def get_systems(db: Session = Depends(get_db)):
    systems = db.exec(select(System)).all()
     
    # SIMILAR TO => SELECT * from System;
    
    return systems

@app.get("/system/{system_id}", response_model=System, status_code=200)
def get_one_system(system_id: int, db: Session = Depends(get_db)):
    one_system = db.get(System, system_id)
    if not one_system:
        raise HTTPException(status_code=404, detail="System not found")
    return one_system


from pydantic import BaseModel

class Check_in_request(BaseModel):
    student_id_str: str
    
    
@app.post('/systems/{system_id}/check-in/', response_model=Booking)
def check_in(system_id: int , request: Check_in_request, db: Session = Depends(get_db)):

        # Get the system details
        system = db.get(System, system_id)

        if not system:
            raise HTTPException(status_code=404, detail="System not found")
    
        student = db.exec(select(Student).where(Student.student_rollNo == request.student_id_str)).first()
        
        new_booking = Booking(student_id=student.student_id, system_id=system.system_id)
        
        db.add(new_booking)
        db.commit()
        
        system.current_booking_id = new_booking.booking_id
        db.add(system)
        db.commit()
        db.refresh(new_booking)
        
        return new_booking
    
    
from datetime import datetime

@app.post('/systems/{system_id}/check-out/', response_model=Booking)
def check_out(system_id: int, db: Session = Depends(get_db)):
    system = db.get(System, system_id)
    
    if not system and system.current_booking_id is None:
        raise HTTPException(404, "System currently not in use")
    
    booking = db.get(Booking, system.current_booking_id)
    booking.check_out_time = datetime.now()
    db.add(booking)
    
    system.current_booking_id = None
    db.add(system)
    db.commit()
    db.refresh(booking)
    
    return booking
       
