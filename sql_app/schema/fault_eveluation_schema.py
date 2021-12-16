
from typing import Optional
from pydantic import BaseModel

class FaultSchema(BaseModel):
    id: Optional[str]
    reason: str
    category: str
    workplace: str
    department: str
    product: str
    dispolevel: str
    estimated_down_time: Optional[int]

    class Config:
        orm_mode = True

