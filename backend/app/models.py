from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class ContentStatus(str, enum.Enum):
    planned = "planned"
    generating = "generating"
    needs_review = "needs_review"
    approved = "approved"
    scheduled = "scheduled"
    publishing = "publishing"
    posted = "posted"
    failed = "failed"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    contents = relationship("Content", back_populates="owner")

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_name = Column(String)
    s3_key = Column(String, unique=True, index=True)
    url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Content(Base):
    __tablename__ = "contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(SQLEnum(ContentStatus), default=ContentStatus.planned)
    owner_id = Column(Integer, ForeignKey("users.id"))
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    
    # Scheduling info
    publish_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Metadata for posted
    platform_post_id = Column(String, nullable=True) 

    owner = relationship("User", back_populates="contents")
    asset = relationship("Asset")

