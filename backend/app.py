from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import *

sqlite_file_name    = "database.db"
sqlite_url          = f"sqlite:///{sqlite_file_name}"

# in prod remove echo
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_samples():
    with Session(engine) as session:
        # Insert MacroCycle
        macrocycle = MacroCycle(
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            goal="Increase Overall Strength and Endurance",
            pillar="Physical"
        )
        session.add(macrocycle)
        session.commit()

        # Insert MesoCycles
        mesocycles = [
            MesoCycle(start_date=date(2024, 1, 1), end_date=date(2024, 3, 31), theme="Strength Foundation", macrocycle_id=macrocycle.id),
            MesoCycle(start_date=date(2024, 4, 1), end_date=date(2024, 6, 30), theme="Hypertrophy & Volume", macrocycle_id=macrocycle.id),
        ]
        session.add_all(mesocycles)
        session.commit()

        # Insert MicroCycles
        microcycles = [
            MicroCycle(start_date=date(2024, 1, 1), end_date=date(2024, 1, 31), focus="Baseline Testing", mesocycle_id=mesocycles[0].id),
            MicroCycle(start_date=date(2024, 2, 1), end_date=date(2024, 2, 29), focus="Strength Progression", mesocycle_id=mesocycles[0].id),
        ]
        session.add_all(microcycles)
        session.commit()

def filter_macrocycles():
    with Session(engine) as session:
        statement = select(Macrocycles).where(Macrocycles.year == "2025")
        results = session.exec(statement)
        print(f"\n2025 Plan found: {results}")
        breakpoint()

def main():
    create_db_and_tables()
    create_samples()

if __name__ == "__main__":
    main()
