from pydantic import BaseModel

class IPLocation(BaseModel):
    start: str
    end: str
    country_code: str