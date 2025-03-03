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


class GoalCycles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    macro_id: int
    meso_id: int
    micro_id: int
    goal_name: str


class StrengthBase(SQLModel):
    workout: str # push one,pull
    target: str #chest -> probably becomes actual msucle names
    name: str
    sets: int
    reps: int
    rpe: int
    weight: int
    effort: str # "6,6,6,6"
    date: str = Field(default=date.today())

class Strength(StrengthBase, table=True):
    id: int = Field(default=None, primary_key=True)

class StrengthCreate(StrengthBase):
    pass

class StrengthPublic(StrengthBase):
    id: int

class RecoveryBase(SQLModel):
    workout: str # yoga, Nerve Glides, mobility, foam rolling,
    target: str #chest -> probably becomes actual msucle names
    name: str
    sets: int
    reps: int
    rpe: int
    weight: int
    effort: str # "6,6,6,6"
    date: str = Field(default=date.today())

class Recovery(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # this needs to be hidden in the post API

class RecoveryCreate(RecoveryBase):
    pass

class RecoveryPublic(RecoveryBase):
    id: int

class Endurance(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # this needs to be hidden in the post API
    workout: str
    length: str
    distance: str
    effort: int
    date: str = Field(default=date.today())


class Flexibility(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # this needs to be hidden in the post API
    workout: str # yoga, Nerve Glides, mobility, foam rolling,
    target: str #chest -> probably becomes actual msucle names
    name: str
    style: str
    length: str # wants to be time
    date: str = Field(default=date.today())
