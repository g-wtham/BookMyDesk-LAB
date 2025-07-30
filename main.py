from fastapi import FastAPI
from models import System, Student
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

@app.get("/systems/", response_model=List[System], status_code=200)
def get_systems(db: Session = Depends(get_db)):
    systems = db.exec(select(System)).all()
    return systems

@app.get("/system/{system_id}", response_model=System, status_code=200)
def get_one_system(system_id: int, db: Session = Depends(get_db)):
    one_system = db.get(System, system_id)
    if not one_system:
        raise HTTPException(status_code=404, detail="System not found")
    return one_system




     