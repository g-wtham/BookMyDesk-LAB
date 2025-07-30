from sqlmodel import create_engine, Session, SQLModel, Field

database_url = 'sqlite:///./computer_lab.db'
engine = create_engine(database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_db():
    with Session(engine) as session:
        yield session
       
# You are giving the database, and getting a session to connect to the DB  