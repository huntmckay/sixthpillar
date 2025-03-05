from enum import Enum
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select, col
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

@app.post("/trackers/", response_model=TrackerPublic)
def create_tracker(tracker: TrackerCreate):
    with Session(engine) as session:
        db_tracker = Tracker.model_validate(tracker)
        session.add(db_tracker)
        session.commit()
        session.refresh(db_tracker)
        return db_tracker

@app.get("/trackers/", response_model=list[TrackerPublic])
def read_tracker():
    with Session(engine) as session:
        tracker = session.exec(select(Tracker)).all()
        return tracker

# Hey its me, turns out that session.get() only works with ID's
@app.get("/trackers/{tracker_name}")
def get_tracker_by_name(tracker_name: str):
    with Session(engine) as session:
        statement = select(Tracker).where(Tracker.name == tracker_name)
        results = session.exec(statement).all()

        if not results:
            raise HTTPException(status_code=404, detail="tracker not found")

        return results

@app.post(f"/strength/", response_model=StrengthPublic)
def create_exercise(exercise: StrengthCreate):
    with Session(engine) as session:
        db_exercise = Strength.model_validate(exercise)
        session.add(db_exercise)
        session.commit()
        session.refresh(db_exercise)
        return db_exercise

@app.get("/strength/", response_model=list[StrengthPublic])
def read_exercises():
    with Session(engine) as session:
        exercise = session.exec(select(Strength)).all()
        return exercise
