import ipaddress
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorCollection
from persistence import get_db
from services import DataPullingService

router = APIRouter()


@router.get('/api/country/{ip_address}')
async def get_country(ip_address: str, db: AsyncIOMotorCollection = Depends(get_db)):
    try:
        ip_int_array = DataPullingService.ip_to_int_array(ip_address)
        result = await db.find_one({
            'start': {'$lte': ip_int_array},
            'end': {'$gte': ip_int_array},
        })
        
        if result is not None:
            return result['country_code']
        return None
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


