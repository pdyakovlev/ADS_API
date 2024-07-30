from app.api.ad import router as ad_router
from app.core.config import settings
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title=settings.app_title, description=settings.desc)
app.include_router(ad_router)
