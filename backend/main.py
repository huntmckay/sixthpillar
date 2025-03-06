import pdb
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date
from models import *

sqlite_file_name    = "database.db"
sqlite_url          = f"sqlite:///{sqlite_file_name}"
connect_args        = {"check_same_thread": False}

# in prod remove echo
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        # yield keyword returns a list, return only returns a single value
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/trackers/", response_model=TrackerPublic)
def create_tracker(*, session: Session = Depends(get_session),tracker: TrackerCreate):
    db_tracker = Tracker.model_validate(tracker)
    session.add(db_tracker)
    session.commit()
    session.refresh(db_tracker)
    return db_tracker


@app.get("/trackers/", response_model=list[TrackerPublic])
def read_tracker(*, session: Session = Depends(get_session)):
    tracker = session.exec(select(Tracker)).all()
    return tracker


@app.get("/trackers/{tracker_name}")
def get_tracker_by_name(*, session: Session=Depends(get_session), tracker_name: str):
    statement = select(Tracker).where(Tracker.name == tracker_name)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="tracker not found")
    return results


@app.post("/strength/", response_model=StrengthPublic)
def create_exercise(*, session: Session=Depends(get_session), exercise: StrengthCreate):
    db_exercise = Strength.model_validate(exercise)
    session.add(db_exercise)
    session.commit()
    session.refresh(db_exercise)
    return db_exercise

@app.get("/strength/", response_model=list[StrengthPublic])
def read_exercises(*, session: Session=Depends(get_session)):
    exercise = session.exec(select(Strength)).all()
    return exercise

@app.get("/strength/{workout_date}", response_model=list[StrengthPublic])
def get_exercise_by_date(*, session: Session=Depends(get_session), workout_date: date):
    statement = select(Strength).where(Strength.date == workout_date)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail=f"No exercises on {date}")
    return results
