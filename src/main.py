from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from persistence import get_db
from services import DataPullingService
from api import router

app = FastAPI()
scheduler = AsyncIOScheduler()
scheduler.start()

@app.on_event("startup")
async def startup_event():
    db = await get_db()
    service = DataPullingService(db)
    await service.fill_data_from_uploaded(1000)
    scheduler.add_job(service.pulling_task, 'interval', hours=1)

app.include_router(router)