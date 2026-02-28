from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Content, ContentStatus
from pydantic import BaseModel

router = APIRouter()

class ContentGeneratedPayload(BaseModel):
    content_id: int
    asset_url: str

class ContentPublishedPayload(BaseModel):
    content_id: int
    platform_post_id: str

@router.post("/n8n/content-generated")
def content_generated(payload: ContentGeneratedPayload, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.id == payload.content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    
    # Update content status and asset URL (simple logic for now)
    content.status = ContentStatus.needs_review
    # In a real app we would update the asset record, but for MVP minimal
    print(f"Content {content.id} generated with asset {payload.asset_url}")
    db.commit()
    return {"status": "success"}

@router.post("/n8n/content-published")
def content_published(payload: ContentPublishedPayload, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.id == payload.content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    content.status = ContentStatus.posted
    content.platform_post_id = payload.platform_post_id
    db.commit()
    return {"status": "success"}

@router.post("/n8n/analytics-synced")
def analytics_synced(data: dict):
    print(f"Analytics synced: {data}")
    return {"status": "success"}
