# models/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import enum
import datetime

class SubscriptionStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    features = Column(String)
    duration = Column(Integer)  # in days

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(Enum(SubscriptionStatus), default=SubscriptionStatus.ACTIVE)

    plan = relationship("Plan")
