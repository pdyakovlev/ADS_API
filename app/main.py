from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.ad import router as ad_router
from app.api.user import router as user_router
from app.core.config import settings

load_dotenv()

app = FastAPI(title=settings.app_title, description=settings.desc)
app.include_router(ad_router)
app.include_router(user_router)
