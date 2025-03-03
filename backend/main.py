from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date
from models import *

sqlite_file_name    = "database.db"
sqlite_url          = f"sqlite:///{sqlite_file_name}"
connect_args        = {"check_same_thread": False}

# in prod remove echo
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/exercises/strength/", response_model=StrengthPublic)
def create_exercise(exercise: StrengthCreate):
    with Session(engine) as session:
        db_exercise = Strength.model_validate(exercise)
        session.add(db_exercise)
        session.commit()
        session.refresh(db_exercise)
        return db_exercise

@app.get("/exercises/strength/", response_model=list[StrengthPublic])
def read_exercises():
    with Session(engine) as session:
        exercise = session.exec(select(Strength)).all()
        return exercise
