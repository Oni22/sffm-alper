
from pydantic import BaseModel

class FaultSchema(BaseModel):
    reason: str
    category: str
    workplace: str
    department: str
    product: str
    dispolevel: str
    timestamp: str
    estimated_down_time: int

    class Config:
        orm_mode = True

