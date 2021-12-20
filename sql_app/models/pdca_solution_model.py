
from sqlalchemy.sql.sqltypes import ARRAY, Integer
from sql_app.models.base_model import BaseModel
from sqlalchemy import Column, String


class PDCASolutionModel(BaseModel):
    __table_args__ = {'schema': 'alon'}
    __tablename__ = "pdca"

    def __init__(self,username=None,currentPhase=None, duration=None,id=None, title=None, titleTags=None, newCauses=None, category=None, downtime=None, shortTimeAction=None, longTimeAction=None, resources=None, goals=None, results=None, specifications=None, standards=None, timestamp=None):

        if id is None:
            self.id = self.create_uuid()
        else:
            self.id = id

        self.title = title
        self.title_tags = titleTags
        self.new_causes = newCauses
        self.category = category
        self.downtime = downtime
        self.resources = resources
        self.short_time_actions = shortTimeAction
        self.long_time_actions = longTimeAction
        self.results = results
        self.specifications = specifications
        self.goals = goals
        self.standards = standards
        self.username = username
        self.current_phase = currentPhase
        self.duration = duration
        self.timestamp = timestamp

    id = Column(String, primary_key=True)
    title = Column(String, nullable=True)
    title_tags = Column(ARRAY(String), nullable=True)
    new_causes = Column(ARRAY(String), nullable=True)
    downtime = Column(String, nullable=True)
    short_time_actions = Column(ARRAY(String), nullable=True)
    long_time_actions = Column(ARRAY(String), nullable=True)
    resources = Column(ARRAY(String), nullable=True)
    goals = Column(ARRAY(String), nullable=True)
    results = Column(ARRAY(String), nullable=True)
    specifications = Column(ARRAY(String), nullable=True)
    standards = Column(ARRAY(String), nullable=True)
    username = Column(String, nullable=True)
    current_phase = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    timestamp = Column(String, nullable=True)
