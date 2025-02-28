from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, List

class Tracker(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    metric: str
    complexity: str
    source: str
    storage: str
    entry_method: str
    description: str | None = Field(default=str("No Description set"))

# a workout session is jsut going to be a filter of date

class Exercise(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    workout: str # push one,pull
    target: str #chest -> probably becomes actual msucle names
    name: str
    sets: int
    reps: int
    rpe: int
    weight: int
    effort: str # "6,6,6,6"
    date: date
