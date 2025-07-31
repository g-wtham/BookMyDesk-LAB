from sqlmodel import SQLModel, Field

class System(SQLModel, table=True):
    system_id: int = Field(primary_key=True)
    system_name : str
    system_location : str
    
    currently_inUse: bool
    
    
class Student(SQLModel, table=True):
    student_id: int = Field(primary_key=True)
    student_name: str
    student_rollNo : str
    student_dept: str
    student_year: int
    student_section: str
    
from datetime import datetime
from sqlmodel import Optional

class Booking(SQLModel, table=True):
    booking_id: Optional[int] = Field(default=None, primary_key=True)
    check_in_time: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    check_out_time: Optional[datetime] = Field(default=None)
    
    student_id: int = Field(foreign_key="student.student_id")
    system_id: int = Field(foreign_key="system.system_id")
    


