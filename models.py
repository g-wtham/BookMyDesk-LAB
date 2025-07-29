from sqlmodel import SQLModel, Field

class System(SQLModel, table=True):
    system_id: int = Field(primary_key=True)
    system_name : str
    system_location : str
    
    
class Student(SQLModel, table=True):
    system_id: int = Field(primary_key=True)
    student_name: str
    student_rollNo : str
    student_dept: str
    student_year: int
    student_section: str
    


