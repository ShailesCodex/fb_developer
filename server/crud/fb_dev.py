from typing import List, Optional, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from server.crud.base import CRUDBase
from server.models.fb_dev import Campaign
from server.schemas.fb_dev import CampaignCreate, CampaignUpdate

UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDCAMPAIGN(CRUDBase[Campaign, CampaignCreate, CampaignUpdate]):
    filter_options = ["amount, number of generations"]

    def get_all(self, db: Session) -> List[Campaign]:
        return db.query(Campaign).all()

    def get_by_id(self, db: Session, *, id: str) -> Campaign:
        return db.query(Campaign).filter(Campaign.id == id).first()

    def get_by_fb_uid(self, db: Session, *, firebase_id: str) -> Campaign:
        return db.query(Campaign).filter(Campaign.firebase_id == firebase_id).first()

    def get_by_email(self, db: Session, *, email: str) -> Campaign:
        return db.query(Campaign).filter(Campaign.email == email).first()

    def create(self, db: Session, *, obj_in: CampaignCreate) -> Campaign:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: Campaign, obj_in: CampaignUpdate) -> Campaign:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, *, id: str) -> Optional[Campaign]:
        return super().remove(db, id=id)


campaign = CRUDCAMPAIGN(Campaign)
