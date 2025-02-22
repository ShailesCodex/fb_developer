from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Float, Text, JSON,ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from server.db import Base


class Campaign(Base):
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(String)
    bid_strategy = Column(String)
    budget_schedule_specs = Column(String)
    buying_type = Column(String)  # AUCTION, RESERVED
    daily_budget = Column(Integer)
    lifetime_budget = Column(Integer)
    name = Column(String, nullable=False)
    is_skadnetwork_attribution = Column(Boolean)
    objective = Column(String)
    special_ad_categories = Column(JSON)
    special_ad_category_country = Column(JSON)
    spend_cap = Column(Integer)
    status = Column(String, default="ACTIVE")  # ACTIVE, PAUSED, DELETED
    
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ad_sets = relationship("AdSet", back_populates="campaign")

    # budget = Column(String)   # daily_budget, lifetime_budget
    # amount = Column(Integer)

class AdSet(Base):
    __tablename__ = "ad_sets"
    
    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    bid_amount = Column(Integer)
    bid_strategy = Column(String)
    billing_event = Column(String)
    budget_schedule_specs = Column(JSON)
    daily_budget = Column(Integer)
    daily_min_spend_target = Column(Integer)
    daily_spend_cap = Column(Integer)
    destination_type = Column(String)
    lifetime_budget = Column(Integer)
    lifetime_min_spend_target = Column(Integer)
    lifetime_spend_cap = Column(Integer)
    name = Column(String, nullable=False)
    optimization_goal = Column(String)
    status = Column(String, default="ACTIVE")  # ACTIVE, PAUSED, DELETED, ARCHIVED
    targeting = Column(JSON, nullable=True)  # JSON serialized targeting details
    tune_for_category = Column(String)
    time_start = Column(DateTime)
    time_stop = Column(DateTime)
    
    # end_time = Column(DateTime)  # Required when lifetime_budget is specified.
    # start_time = Column(DateTime)   # The start time of the set.
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    campaign = relationship("Campaign", back_populates="ad_sets")
    ads = relationship("Ad", back_populates="ad_set")


class AdCreative(Base):
    __tablename__ = "ad_creatives"
    
    id = Column(Integer, primary_key=True, index=True)
    authorization_category = Column(String)
    body = Column(String)
    call_to_action_type = Column(String)
    name = Column(String)
    object_story_id = Column(String)
    object_story_spec = Column(JSON)
    object_type = Column(String)
    status = Column(String, default="ACTIVE")  # ACTIVE, IN_PROCESS, WITH_ISSUES, DELETED
    title = Column(String)
        
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ads = relationship("Ad", back_populates="creative")


class Ad(Base):
    __tablename__ = "ads"
    
    id = Column(Integer, primary_key=True, index=True)
    ad_schedule_end_time = Column(DateTime)   # This parameter is only available for sales and app promotion campaigns.
    ad_schedule_start_time = Column(DateTime)   # This parameter is only available for sales and app promotion campaigns.
    
    name = Column(String, nullable=False)
    ad_set_id = Column(Integer, ForeignKey("ad_sets.id"), nullable=False)
    creative_id = Column(Integer, ForeignKey("ad_creatives.id"), nullable=False)
    status = Column(String, default="ACTIVE")  # ACTIVE, PAUSED, DELETED, ARCHIVED

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    ad_set = relationship("AdSet", back_populates="ads")
    creative = relationship("AdCreative", back_populates="ads")

