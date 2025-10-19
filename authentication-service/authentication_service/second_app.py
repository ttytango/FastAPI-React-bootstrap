from fastapi import FastAPI
from authentication_service.config import configure, get_settings

app = FastAPI(title="Another API")

configure()
settings = get_settings()

@app.get("/ping")
async def ping():
    return {"ok": True, "env": settings.environment}


