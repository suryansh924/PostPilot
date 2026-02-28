from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Content as ContentModel, User, ContentStatus
from app.schemas import ContentCreate, Content, ContentUpdate
from app.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=Content)
def create_content(content: ContentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_content = ContentModel(**content.dict(), owner_id=current_user.id)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

@router.get("/", response_model=List[Content])
def read_contents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contents = db.query(ContentModel).filter(ContentModel.owner_id == current_user.id).offset(skip).limit(limit).all()
    return contents

@router.get("/{content_id}", response_model=Content)
def read_content(content_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    content = db.query(ContentModel).filter(ContentModel.id == content_id, ContentModel.owner_id == current_user.id).first()
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.patch("/{content_id}/status", response_model=Content)
def update_content_status(content_id: int, status: ContentStatus, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    content = db.query(ContentModel).filter(ContentModel.id == content_id, ContentModel.owner_id == current_user.id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    # For MVP just update status directly
    content.status = status
    db.commit()
    db.refresh(content)
    return content
