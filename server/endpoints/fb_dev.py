import random
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
import requests
from sqlalchemy.orm import Session
from server import crud, schemas
from server.db import get_db
from server.models.fb_dev import Campaign


camp_router = APIRouter(prefix="/campaign", tags=["Campaign"])



@camp_router.get("/")
async def get_campaign():
    try:
        
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "error": None,
                "data": profile.dict(),
                "message": "User profile fetched successfully.",
            },
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": str(e.detail),
                "message": str(e.detail),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "data": None,
                "error": str(e),
                "message": "Something went wrong!",
            },
        )


@camp_router.post("/")
async def create_campaign(data: schemas.CampaignCreate, db: Session = Depends(get_db)):
    try:
        
        url = "https://graph.facebook.com/v22.0/act_515880804441941/campaigns"
        
        payload = {key: value for key, value in data.dict(exclude_unset=True).items() if value is not None}


        payload["access_token"] = "EAAdEJ4ZAijhABO8M0HGh3qghnG1vlQfFZBFkvDYYP5aROcw8M2kYqVbhVUZBaAIGWdN3ndwXn3d8HxdnbIl5xE05XzC4y8sFmmYAVHvGZBOcaOR7d2SFvmAX6X3bCVaaJZCSzZA1FWBeMZCRUxwcIstNgMZBWmyKcorPMT1EhGxQ2PdlAoKwYKKNNSghtd4mHtfksMeMXaAZD"

        headers = {"Content-Type": "application/json"}

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            fb_response = response.json()
            campaign_id = fb_response.get("id")
            
            new_campaign = Campaign(
                campaign_id=campaign_id,
                bid_strategy=data.bid_strategy,
                budget_schedule_specs=data.budget_schedule_specs,
                buying_type=data.buying_type,
                daily_budget=data.daily_budget,
                lifetime_budget=data.lifetime_budget,
                name=data.name,
                is_skadnetwork_attribution=data.is_skadnetwork_attribution,
                objective=data.objective,
                special_ad_categories=data.special_ad_categories,
                special_ad_category_country=data.special_ad_category_country,
                spend_cap=data.spend_cap,
                status=data.status,
                start_date=data.start_date,
                end_date=data.end_date,
            )

            db.add(new_campaign)
            db.commit()
            db.refresh(new_campaign)
            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "error": None,
                    "data": response.json(),
                    "message": "Campaign created successfully",
                },
            )
        else:
            return JSONResponse(
                status_code=response.status_code,
                content={
                    "success": False,
                    "error": response.json(),
                    "message": "Failed to create campaign",
                },
            )


    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": str(e.detail),
                "message": str(e.detail),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "data": None,
                "error": str(e),
                "message": "Something went wrong!",
            },
        )

    finally:
        db.close()
