import ipaddress
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection
from persistence import get_db

router = APIRouter()

@router.get('/api/country/{ip_address}')
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

