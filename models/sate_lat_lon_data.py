from pydantic import BaseModel


class SateLatLonData(BaseModel):
    name: str
    latitude: float
    longitude: float
    altitude: float
