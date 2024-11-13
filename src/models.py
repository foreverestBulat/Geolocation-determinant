from pydantic import BaseModel

class IPLocation(BaseModel):
    start: int
    end: int
    country_code: str