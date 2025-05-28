# routes/subscription_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import SubscriptionCreate, SubscriptionOut, PlanOut
from app.services.subscription_service import *
from app.database import SessionLocal

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SubscriptionOut)
def subscribe(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    return create_subscription(db, subscription)

@router.get("/{user_id}", response_model=SubscriptionOut)
def get_subscription(user_id: int, db: Session = Depends(get_db)):
    return get_user_subscription(db, user_id)

@router.put("/{user_id}", response_model=SubscriptionOut)
def update_user_subscription(user_id: int, plan_id: int, db: Session = Depends(get_db)):
    return update_subscription(db, user_id, plan_id)

@router.delete("/{user_id}", response_model=SubscriptionOut)
def delete_user_subscription(user_id: int, db: Session = Depends(get_db)):
    return cancel_subscription(db, user_id)

@router.get("/plans", response_model=list[PlanOut])
def list_plans(db: Session = Depends(get_db)):
    return get_all_plans(db)

