from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


# class CampaignBase(BaseModel):
#     avatar: Optional[str] = None
#     email: Optional[EmailStr] = None
#     is_verified: Optional[bool] = False
#     is_active: Optional[bool] = False
#     disabled: Optional[bool] = False
#     role: Optional[str] = "member"
#     providers: Optional[str] = None
#     hashed_password: Optional[str] = None
#     is_social: Optional[bool] = False
#     firebase_id: Optional[str] = None
#     device: Optional[str] = None

#     class Config:
#         from_attributes = True


class CampaignCreate(BaseModel):
    bid_strategy: Optional[str] = None
    budget_schedule_specs: Optional[str] = None
    buying_type: Optional[str] = None
    daily_budget: Optional[int] = None
    lifetime_budget: Optional[int] = None
    name: Optional[str] = None
    is_skadnetwork_attribution: Optional[bool] = False
    objective: Optional[str] = None
    special_ad_categories: Optional[List[str]] = None
    special_ad_category_country: Optional[List[str]] = None
    spend_cap: Optional[int] = None
    status: Optional[str] = "ACTIVE"  # ACTIVE, PAUSED, DELETED
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class CampaignUpdate(BaseModel):
    pass

