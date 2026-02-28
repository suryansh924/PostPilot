from fastapi import APIRouter, Depends, UploadFile, File
from app.deps import get_current_user
from app.s3 import create_presigned_post
from app.models import User
import uuid

router = APIRouter()

from app.schemas import S3PresignedPost

@router.post("/content/upload-url", response_model=S3PresignedPost)
def get_upload_url(filename: str, current_user: User = Depends(get_current_user)):
    ext = filename.split(".")[-1]
    object_name = f"{current_user.id}/{uuid.uuid4()}.{ext}"
    response = create_presigned_post(object_name)
    return response
