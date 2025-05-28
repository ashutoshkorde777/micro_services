# services/subscription_service.py
from sqlalchemy.orm import Session
from app.models.models import Subscription, Plan, SubscriptionStatus
from app.schemas.schemas import SubscriptionCreate
import datetime

def create_subscription(db: Session, subscription: SubscriptionCreate):
    plan = db.query(Plan).filter(Plan.id == subscription.plan_id).first()
    new_subscription = Subscription(
        user_id=subscription.user_id,
        plan_id=subscription.plan_id,
        start_date=datetime.datetime.utcnow(),
        status=SubscriptionStatus.ACTIVE
    )
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription

def get_user_subscription(db: Session, user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).first()

def update_subscription(db: Session, user_id: int, plan_id: int):
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if subscription:
        subscription.plan_id = plan_id
        subscription.start_date = datetime.datetime.utcnow()
        subscription.status = SubscriptionStatus.ACTIVE
        db.commit()
        db.refresh(subscription)
    return subscription

def cancel_subscription(db: Session, user_id: int):
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if subscription:
        subscription.status = SubscriptionStatus.CANCELLED
        db.commit()
        db.refresh(subscription)
    return subscription

def get_all_plans(db: Session):
    return db.query(Plan).all()
