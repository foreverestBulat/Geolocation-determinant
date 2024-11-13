from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import geocoder
from fastapi import FastAPI

app = FastAPI()


@app.get('/api/country/{ip_address}')
async def get_country(ip_address: str):
    
    
    
    return ip_address

@app.post("/geolocate")
async def geolocate(request: Request):
    """
    Получает IP-адрес из запроса и возвращает геолокацию.
    """
    ip_address = request.client.host
    g = geocoder.ip(ip_address)

    if g.ok:
        return JSONResponse({
            "city": g.city,
            "country": g.country,
            "latitude": g.latlng[0],
            "longitude": g.latlng[1]
        })
    else:
        return JSONResponse({"error": "Не удалось определить геолокацию."}, status_code=400)