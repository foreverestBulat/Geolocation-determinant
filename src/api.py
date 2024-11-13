import ipaddress
import asyncio
from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorCollection
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from persistence import get_db
from services import DataPullingService

app = FastAPI()
scheduler = AsyncIOScheduler()
scheduler.start()

@app.on_event("startup")
async def startup_event():
    db = get_db()
    service = DataPullingService(db)
    await service.pulling_task()
    # asyncio.create_task(service.pulling_task()) # чтобы начать сразу заполнять
    scheduler.add_job(service.pulling_task, 'interval', hours=1)

@app.get('/api/country/{ip_address}')
async def get_country(ip_address: str, db: AsyncIOMotorCollection = Depends(get_db)):
    ip_address_int = int.from_bytes(ipaddress.ip_address(ip_address).packed, byteorder='big')
    
    result = await db.find_one({
        'start': {
            '$lte': ip_address_int
        },
        'end': {
            '$gte': ip_address_int
        }
    })
    
    if result is not None:
        return result['country_code']
    
    return None