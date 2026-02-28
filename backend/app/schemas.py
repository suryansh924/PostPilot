from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ContentStatus(str, Enum):
    planned = "planned"
    generating = "generating"
    needs_review = "needs_review"
    approved = "approved"
    scheduled = "scheduled"
    publishing = "publishing"
    posted = "posted"
    failed = "failed"

class ContentBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: ContentStatus = ContentStatus.planned
    publish_at: Optional[datetime] = None

class ContentCreate(ContentBase):
    pass

class ContentUpdate(ContentBase):
    pass

class Content(ContentBase):
    id: int
    owner_id: int
    asset_id: Optional[int] = None
    platform_post_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class S3PresignedPost(BaseModel):
    url: str
    fields: dict
