
from typing import List, Optional
from pydantic import BaseModel

class PDCASchema(BaseModel):
    title: Optional[str]
    id: Optional[str]
    title_tags: Optional[List[str]]
    new_causes: Optional[List[str]]
    category: Optional[str]
    downtime: Optional[str]
    resources: Optional[List[str]]
    short_time_actions: Optional[List[str]]
    long_time_actions: Optional[List[str]]
    results: Optional[List[str]]
    specifications: Optional[List[str]]
    goals: Optional[List[str]]
    standards: Optional[List[str]]
    username: Optional[str]
    duration: Optional[str]
    current_phase: Optional[str]

    class Config:
        orm_mode = True

