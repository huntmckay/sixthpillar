from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, List

class MacroCycle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    start_date: date
    end_date: date
    pillar: str
    goal: str
    mesocycles: List["MesoCycle"] = Relationship(back_populates="macrocycle")

class MesoCycle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    macrocycle_id: int = Field(foreign_key="macrocycle.id")
    start_date: date
    end_date: date
    theme: str
    macrocycle: Optional[MacroCycle] = Relationship(back_populates="mesocycles")
    microcycles: List["MicroCycle"] = Relationship(back_populates="mesocycle")

class MicroCycle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    mesocycle_id: int = Field(default=None, foreign_key="mesocycle.id")
    start_date: date
    end_date: date
    focus: str
    mesocycle: Optional[MesoCycle] = Relationship(back_populates="microcycles")
    #daily_logs: List["PhysicalLog"] = Relationship(back_populates="microcycle")
