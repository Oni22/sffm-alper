from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.requests import Request
from dependencies import get_db
from sql_app.models.fault_evaluation_model import FaultEvaluationModel
import datetime
from sql_app.schema.dt_schema import DTSchema
from utils import workspace, faultReason, products
from sql_app.schema.fault_eveluation_schema import FaultSchema
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#nodejs

router = APIRouter(
    prefix="/fault",
)



@router.post("",response_model=FaultSchema,status_code=200)
def addFault(faultRequest: FaultSchema):
    
    try:
        fault = FaultEvaluationModel(
            reason=faultReason.faultReason[faultRequest.reason] if faultRequest.reason in faultReason.faultReason  else "unknown",
            category=faultRequest.category,
            workplace= workspace.workspace[faultRequest.workplace] if faultRequest.workplace in workspace.workspace   else "unknown",
            department=faultRequest.department,
            product=products.products[faultRequest.product] if faultRequest.product in products.products else "unknown",
            dispolevel=faultRequest.dispolevel,
            timestamp=datetime.datetime.now().isoformat(),
            # estimated_down_time=faultRequest.estimated_down_time
            )
        fault.save()
        return fault
    except Exception as e:
        print(e)
        raise HTTPException(detail=str(e),status_code=400)


@router.get("/{fault_id}",response_model=FaultSchema,status_code=200)
def getFault(fault_id: str,db : Session = Depends(get_db)):
    fault = db.query(FaultEvaluationModel).filter_by(id=fault_id).first()
    return fault


@router.get("",status_code=200)
def getAllFaults(db : Session = Depends(get_db)):
    faults = db.query(FaultEvaluationModel).all()
    return faults

@router.post("/analyze",status_code=200)
def analyzeFault(dtSchema: DTSchema):
    reason = int(dtSchema.reason)
    workplace = int(dtSchema.workplace)
    product = int(dtSchema.product)

    database = pd.read_csv('stoerungsauswertung.csv',delimiter=';')
    features = ['Fehlergrund', 'Arbeitsgang','Produkt']
    x = database[features]
    y = database['Maßnahme']
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x,y)
    pred = clf.predict([[reason,workplace,product]])

    X = database.iloc[:, [0,2]].values  
    y = database.iloc[:, 8].values
    classifier2 = KNeighborsClassifier(n_neighbors=6) 
    classifier2.fit(X,y)
    knn = classifier2.predict([[reason,workplace]])

    return {
        "action": pred.tolist(),
        "downtime": knn.tolist()
    }