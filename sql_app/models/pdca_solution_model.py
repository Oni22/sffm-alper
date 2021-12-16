
# from sqlalchemy.sql.sqltypes import Integer
# from sql_app.models.base_model import BaseModel
# from sqlalchemy import Column, String


# class pdcaSolutionModel(BaseModel):
#     __table_args__ = {'schema': 'alon'}
#     __tablename__= "pdca_solution"

#     def __init__(self,id=None,title=None,titleTags=None,newCauses=None,category=None,estimated_down_time=None,shortTimeAction=None,longTimeAction=None,ressources=None,goals=None,results=None,specifications=None,standards=None,timestamp=None):
    
#         if id is None:
#             self.id = self.create_uuid()
#         else:
#             self.id = id

#         self.title = title
#         self.titleTags = titleTags
#         self.newCauses = newCauses
#         self.category = category
#         self.estimated_down_time = estimated_down_time
#         self.shortTimeAction = shortTimeAction
#         self.longTimeAction = longTimeAction
#         self.ressources = ressources
#         self.goals = goals
#         self.results = results
#         self.specifications = specifications
#         self.standards = standards
#         #Autor etc angeben!
#         self.timestamp = timestamp


#     id = Column(String,primary_key=True)
#     title = Column(String,nullable=False)
#     titleTags = Column(String,nullable=False)
#     newCauses = Column(String,nullable=False)
#     estimated_down_time = Column(Integer,nullable=False)
#     shortTimeAction = Column(String,nullable=False)
#     longTimeAction = Column(String,nullable=False)
#     ressources = Column(String,nullable=False)
#     goals = Column(String,nullable=False)
#     results = Column(String,nullable=False)
#     specifications = Column(String,nullable=False)
#     standards = Column(String,nullable=False)
#     timestamp = Column(String,nullable=False)

