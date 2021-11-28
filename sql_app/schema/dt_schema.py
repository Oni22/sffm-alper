
from pydantic import BaseModel

class DTSchema(BaseModel):
    reason: str
    workplace: str
    product: str


