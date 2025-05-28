# schemas/schemas.py
from pydantic import BaseModel
from enum import Enum
from typing import Optional
import datetime

class SubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"

class PlanBase(BaseModel):
    name: str
    price: float
    features: str
    duration: int

class PlanOut(PlanBase):
    id: int
    class Config:
        orm_mode = True

class SubscriptionCreate(BaseModel):
    user_id: int
    plan_id: int

class SubscriptionOut(BaseModel):
    id: int
    user_id: int
    plan: PlanOut
    start_date: datetime.datetime
    status: SubscriptionStatus
    class Config:
        orm_mode = True