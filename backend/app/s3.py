import boto3
from botocore.exceptions import ClientError
from app.config import settings
from fastapi import HTTPException
from botocore.config import Config

s3_client = boto3.client(
    's3',
    endpoint_url=settings.AWS_S3_ENDPOINT_URL,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
    config=Config(signature_version='s3v4')
)

def create_presigned_post(object_name, expiration=3600):
    try:
        response = s3_client.generate_presigned_post(
            settings.S3_BUCKET_NAME,
            object_name,
            Fields=None,
            Conditions=None,
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(e)
        raise HTTPException(status_code=500, detail="S3 Error")
    return response
