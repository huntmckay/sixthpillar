from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, List

class TrackerBase(SQLModel):
    pillar: str
    name: str = Field(index=True)
    complexity: str
    source: str
    storage: str
    entry_method: str
    description: str | None = Field(default=str("No Description set"))

class Tracker(TrackerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class TrackerCreate(TrackerBase):
    pass

class TrackerPublic(TrackerBase):
    pass

class TrackerUpdate(TrackerBase):
    pillar: str | None = None
    name: str | None = None
    complexity: str | None = None
    source: str | None = None
    storage: str | None = None
    entry_method: str | None = None
    description: str | None = Field(default=str("No Description set"))

class ExerciseType(str, Enum):
    strength = "strength"
    recovery = "recovery"
    endurance = "endurance"

class ExerciseBase(SQLModel):
    #id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    program: str # push one,pull,yoga, Nerve Glides, mobility, foam rolling,
    date: str = Field(default=date.today())
    notes: str | None = None

class StrengthBase(ExerciseBase, table=True):
    id: int = Field(default=None, primary_key=True)
    target: str #chest -> probably becomes actual msucle names
    sets: int
    reps: int
    rpe: int
    weight: int
    effort: str # "6,6,6,6"

class StrengthExercise(StrengthBase):
    pass

class RecoveryBase(ExerciseBase, table=True):
    id: int = Field(default=None, primary_key=True)
    target: str
    sets: int
    reps: int

class RecoveryExercise(RecoveryBase):
    pass

class EnduranceBase(ExerciseBase, table=True):
    id: int = Field(default=None, primary_key=True)
    length: str
    distance: str
    effort: int # 1-10

class EnduranceExercise(EnduranceBase):
    pass

class GoalCycles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    macro_id: int
    meso_id: int
    micro_id: int
    goal_name: str
