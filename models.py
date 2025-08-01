from sqlmodel import SQLModel, Field
from typing import Optional

class System(SQLModel, table=True):
    system_id: int = Field(primary_key=True)
    system_name : str
    system_location : str
    current_booking_id : Optional[int] = Field(default=None, foreign_key="booking.booking_id")
    
class Student(SQLModel, table=True):
    student_id: int = Field(primary_key=True)
    student_name: str
    student_rollNo : str
    student_dept: str
    student_year: int
    student_section: str
    
from datetime import datetime

class Booking(SQLModel, table=True):
    booking_id: Optional[int] = Field(default=None, primary_key=True)
    
    student_id: int = Field(foreign_key="student.student_id")
    system_id: int = Field(foreign_key="system.system_id")
    check_in_time: datetime = Field(default_factory=datetime.utcnow)
    check_out_time: Optional[datetime]


