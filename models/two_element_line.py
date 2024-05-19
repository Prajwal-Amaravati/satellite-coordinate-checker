from pydantic import BaseModel


class TwoElementLine(BaseModel):
    name: str
    line1: str
    line2: str
