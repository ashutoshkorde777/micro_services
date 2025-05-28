from app.database import SessionLocal
from app.models.models import Plan

# init_db.py (or include this in seed.py before inserting)
from app.database import engine
from app.models import models  # Make sure this import loads your model classes

models.Base.metadata.create_all(bind=engine)


db = SessionLocal()
plan1 = Plan(name="Basic", price=10.0, features="Email Support", duration=30)
plan2 = Plan(name="Premium", price=30.0, features="Chat + Email Support", duration=90)

db.add_all([plan1, plan2])
db.commit()
db.close()
