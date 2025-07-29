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

from sqlmodel import Session
from fastapi import Depends

@app.post("/systems/", response_model=System, status_code=201)
def create_system(system: System, db: Session = Depends(get_db)):
    db.add(system)
    db.commit()
    db.refresh(system)
    return system

@app.post("/students/", response_model=Student, status_code=201)
def create_system(student: Student, db: Session = Depends(get_db)):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student







     