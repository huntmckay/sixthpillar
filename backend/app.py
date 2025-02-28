from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date
from models import *

sqlite_file_name    = "database.db"
sqlite_url          = f"sqlite:///{sqlite_file_name}"

# in prod remove echo
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_samples():
    with Session(engine) as session:
        sub_date=date(2025,2,24)
        push_one_submission = [
            Exercise(workout="push_one",target="chest",name="machine_chest_press",sets=4,reps=6,rpe=9,weight=205,effort="6,6,5,6",date=sub_date),
            Exercise(workout="push_one",target="shoulders",name="barbell_overhead_press",sets=3,reps=8,rpe=8,weight=180,effort="6,6,6",date=sub_date),
            Exercise(workout="push_one",target="chest",name="seated_cable_chest_flyes",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="chest",name="cable_push_downs",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="shoulders",name="cable_lateral_raise",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="core",name="weighted_crunch",sets=3,reps=12,rpe=9,weight=95,effort="12,12,12",date=sub_date),
        ]
        session.add_all(push_one_submission)
        session.commit()
        sub_date=date(2025,3,10)
        push_one_submission = [
            Exercise(workout="push_one",target="chest",name="machine_chest_press",sets=4,reps=6,rpe=9,weight=205,effort="6,6,5,6",date=sub_date),
            Exercise(workout="push_one",target="shoulders",name="barbell_overhead_press",sets=3,reps=8,rpe=8,weight=180,effort="6,6,6",date=sub_date),
            Exercise(workout="push_one",target="chest",name="seated_cable_chest_flyes",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="chest",name="cable_push_downs",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="shoulders",name="cable_lateral_raise",sets=3,reps=8,rpe=8,weight=95,effort="8,8,8",date=sub_date),
            Exercise(workout="push_one",target="core",name="weighted_crunch",sets=3,reps=12,rpe=9,weight=95,effort="12,12,12",date=sub_date),
        ]
        session.add_all(push_one_submission)
        session.commit()
        session.close()

def main():
    create_db_and_tables()
    create_samples()

if __name__ == "__main__":
    main()
