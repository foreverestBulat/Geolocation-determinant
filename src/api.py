import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import geocoder
from fastapi import FastAPI, Depends

import ipaddress

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from motor.motor_asyncio import AsyncIOMotorCollection
from apscheduler.triggers.interval import IntervalTrigger
from persistence import MongoDBClient, get_db
from services import DataPullingService

app = FastAPI()
scheduler = AsyncIOScheduler()
scheduler.start()

@app.on_event("startup")
async def startup_event():
    db = get_db()
    service = DataPullingService(db)
    scheduler.add_job(service.pulling_task, 'interval', hours=1)


@app.get('/api/country/{ip_address}')
async def get_country(ip_address: str, db: AsyncIOMotorCollection = Depends(get_db)):
    ip_int = int(ipaddress.ip_address(ip_address))
    
    documents = await db.find().to_list(length=None)
    
    for document in documents:
        start_ip = ipaddress.ip_address(document["start"])
        end_ip = ipaddress.ip_address(document["end"])
        
        start_int = int(start_ip)
        end_int = int(end_ip)

        if start_int <= ip_int <= end_int:
            return document["country_code"]
    return None