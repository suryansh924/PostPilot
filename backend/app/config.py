from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://neondb_owner:npg_N4VucGLHidw0@ep-mute-mountain-aie5mx8q-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"
    SECRET_KEY: str = "supersecretkey_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 week

    AWS_ACCESS_KEY_ID: str = "minioadmin"
    AWS_SECRET_ACCESS_KEY: str = "minioadmin"
    AWS_REGION: str = "us-east-1"
    AWS_S3_ENDPOINT_URL: str | None = "http://localhost:9000"  # Useful for local minio dev
    S3_BUCKET_NAME: str = "postpilot-media"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
