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
        # Tracking Table
        trackers = [
            Tracker(metric="10000 Steps", source="Garmin", storage="Garmin", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="9PM Bed time", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Caffine", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Creatine", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Food", source="Me", storage="MacroFactor", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Happiness", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Journaling", source="Me", storage="Notion", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Medications", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Meditation", source="Down Dog", storage="Down Dog", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Runs", source="Garmin", storage="Garmin", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Sleep", source="Garmin", storage="Garmin", is_automated=True, synced_to_sixthpillar=False),
            Tracker(metric="Steps", source="Garmin", storage="Garmin", is_automated=True, synced_to_sixthpillar=False),
            Tracker(metric="Stress", source="Garmin and Me", storage="Garmin and Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Water", source="Me", storage="Paper", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Weight", source="Me", storage="MacroFactor", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Workout", source="Notion", storage="Notion", is_automated=False, synced_to_sixthpillar=False),
            Tracker(metric="Yoga", source="Down Dog", storage="Down Dog", is_automated=False, synced_to_sixthpillar=False),
        ]
        session.add_all(trackers)
        session.commit()

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
