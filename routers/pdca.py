
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from sql_app.models.pdca_solution_model import PDCASolutionModel

from sql_app.schema.pdca_eveluation_schema import PDCASchema
from datetime import datetime
from dependencies import get_db

router = APIRouter(
    prefix="/pdca",
)


@router.post("",status_code=200)
def addPDCA(pdcaSchema: PDCASchema):
    print(pdcaSchema)
    try:

        pdca = PDCASolutionModel(
            title=pdcaSchema.title,
            titleTags=pdcaSchema.title_tags,
            newCauses=pdcaSchema.new_causes,
            downtime=pdcaSchema.downtime,
            shortTimeAction=pdcaSchema.short_time_actions,
            longTimeAction=pdcaSchema.long_time_actions,
            resources=pdcaSchema.resources,
            results=pdcaSchema.results,
            specifications=pdcaSchema.specifications,
            standards=pdcaSchema.standards,
            username=pdcaSchema.username,
            currentPhase=pdcaSchema.current_phase,
            duration=pdcaSchema.duration,
            category=pdcaSchema.category,
            timestamp=datetime.now().isoformat(),
            )
        pdca.save()
        return pdca
    except Exception as e:
        print(e)
        raise HTTPException(detail=str(e),status_code=400)    


@router.post("/{pdca_id}",status_code=200,response_model=PDCASchema)
def addPDCA(pdcaSchema: PDCASchema,pdca_id: str,db : Session = Depends(get_db)):
    try:
        pdca = db.query(PDCASolutionModel).filter_by(id=pdca_id).first()
        print(pdca.new_causes)
        
        if pdca is not None:
            pdca.title= pdcaSchema.title if pdcaSchema.title is not None else pdca.title,

            if pdcaSchema.title_tags is not None and len(pdcaSchema.title_tags) > 0:
                pdca.title_tags.extend(pdcaSchema.title_tags),
            
            if pdcaSchema.new_causes is not None and len(pdcaSchema.new_causes) > 0:
                print(pdca.new_causes)
                pdca.new_causes = set(pdca.new_causes + pdcaSchema.new_causes)
                print("HAAAALLLOO")
                print(pdca.new_causes)

            pdca.downtime=pdcaSchema.downtime if pdcaSchema.downtime is not None else pdca.downtime,
            pdca.short_time_actions=pdcaSchema.short_time_actions if pdcaSchema.short_time_actions is not None else pdca.short_time_actions,
            pdca.long_time_actions=pdcaSchema.long_time_actions if pdcaSchema.long_time_actions is not None else pdca.long_time_actions,
            pdca.resources=pdcaSchema.resources if pdcaSchema.resources is not None else pdca.resources,
            pdca.results=pdcaSchema.results if pdcaSchema.results is not None else pdca.results,
            pdca.specifications=pdcaSchema.specifications if pdcaSchema.specifications is not None else pdca.specifications,
            pdca.standards=pdcaSchema.standards if pdcaSchema.standards is not None else pdca.standards,
            pdca.username=pdcaSchema.username if pdcaSchema.username is not None else pdca.username,
            pdca.current_phase=pdcaSchema.current_phase if pdcaSchema.current_phase is not None else pdca.current_phase,
            pdca.duration=pdcaSchema.duration if pdcaSchema.duration is not None else pdca.duration,
            db.commit()
        else:
            return HTTPException(status_code=404)
        print(pdca.new_causes)
        return pdca
    except Exception as e:
        print(e)
        raise HTTPException(detail=str(e),status_code=400)   

@router.get("/{pdca_id}",response_model=PDCASchema,status_code=200)
def getPDCA(pdca_id: str,db : Session = Depends(get_db)):
    solution = db.query(PDCASolutionModel).filter_by(id=pdca_id).first()
    return solution


@router.get("",status_code=200)
def getAllPDCA(db : Session = Depends(get_db)):
    solutions = db.query(PDCASolutionModel).all()
    return solutions