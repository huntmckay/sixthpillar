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
            Tracker(metric="In Bed on time", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Affirmations", complexity="simple", source="I AM", storage="Paper", entry_method="untracked"),
            Tracker(metric="Biking", complexity="complex", source="Garmin", storage="Garmin", entry_method="untracked"),
            Tracker(metric="Creatine", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Endurance today", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Happiness", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Journaled Today", complexity="simple", source="User", storage="Notion", entry_method="manual"),
            Tracker(metric="Limited screen time", complexity="simple", source="iPhone", storage="Paper", entry_method="untracked"),
            Tracker(metric="Medications", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Meditation", complexity="simple", source="Down Dog", storage="Down Dog", entry_method="manual"),
            Tracker(metric="No Caffeine after 2pm", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Runs", complexity="complex", source="Garmin", storage="Garmin", entry_method="untracked"),
            Tracker(metric="Sleep", complexity="complex", source="Garmin", storage="Garmin", entry_method="untracked"),
            Tracker(metric="Sobriety Pledges", complexity="simple", source="I am Sober", storage="Paper", entry_method="untracked"),
            Tracker(metric="Steps", complexity="complex", source="Garmin", storage="Garmin", entry_method="untracked"),
            Tracker(metric="Stress", complexity="complex", source="Garmin", storage="Garmin", entry_method="untracked"),
            Tracker(metric="Stress", complexity="simple", source="User", storage="Paper", entry_method="manual"),
            Tracker(metric="Tracked All Food", complexity="simple", source="User", storage="MacroFactor", entry_method="manual"),
            Tracker(metric="Water", complexity="complex", source="User", storage="MacroFactor", entry_method="manual"),
            Tracker(metric="Weight", complexity="complex", source="User", storage="MacroFactor", entry_method="untracked"),
            Tracker(metric="Workout", complexity="complex", source="Notion", storage="Notion", entry_method="untracked"),
            Tracker(metric="Yoga", complexity="simple", source="Down Dog", storage="Down Dog", entry_method="untracked"),
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
