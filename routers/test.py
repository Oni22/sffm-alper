from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.requests import Request
from dependencies import get_db
from sql_app.models.fault_evaluation_model import FaultEvaluationModel
import datetime
from sql_app.schema.fault_eveluation_schema import FaultSchema

router = APIRouter(
    prefix="/fault",
)

@router.post("",response_model=FaultSchema,status_code=200)
def test(faultRequest: FaultSchema):
    fault = FaultEvaluationModel(
        reason=faultRequest.reason,
        category=faultRequest.category,
        workplace=faultRequest.workplace,
        department=faultRequest.department,
        product=faultRequest.product,
        dispolevel=faultRequest.dispolevel,
        timestamp=datetime.datetime.now().isoformat(),
        estimated_down_time=faultRequest.estimated_down_time
        )
    fault.save()
    return fault


@router.get("/{fault_id}",response_model=FaultSchema,status_code=200)
def test(fault_id: str,db : Session = Depends(get_db)):
    fault = db.query(FaultEvaluationModel).filter_by(id=fault_id).first()
    return fault


@router.get("",status_code=200)
def test(db : Session = Depends(get_db)):
    faults = db.query(FaultEvaluationModel).all()
    return faults


