
from sqlalchemy.sql.sqltypes import ARRAY, Integer
from sql_app.models.base_model import BaseModel
from sqlalchemy import Column, String


class FaultEvaluationModel(BaseModel):
    __table_args__ = {'schema': 'alon'}
    __tablename__= "fault_evaluation"

    def __init__(self,id=None,reason=None,category=None,workplace=None,department=None,product=None,dispolevel=None,timestamp=None,estimated_down_time=None):
    
        if id is None:
            self.id = self.create_uuid()
        else:
            self.id = id

        self.reason = reason
        self.category = category
        self.workplace = workplace
        self.department = department
        self.product = product
        self.dispolevel = dispolevel
        self.timestamp = timestamp
        self.estimated_down_time = estimated_down_time

    id = Column(String,primary_key=True)
    newCauses: Column(ARRAY(String(128)),primary_key=True)
    # category: Array<string> = [];
    # title = Column(String,primary_key=True)
    # downtime = Column(Integer,nullable=False)
    # shortTimeAction: Array<any> = [];
    # longTimeAction: Array<any> = [];
    # ressources: Array<string> = [];
    # goals: Array<string> = [];



