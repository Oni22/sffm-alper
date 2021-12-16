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
# from sql_app.schema.pdca_eveluation_schema import SolutionSchema
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

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

# @router.post("",response_model=SolutionSchema,status_code=200)
# def addPDCA(solutionRequest: SolutionSchema):
    
#     try:
#         fault = SolutionEvaluationModel(
#             title=solutionTitle.solutionTitle[solutionRequest.title] if solutionRequest.title in solutionTitle.solutionTitle  else "unknown",
#             titleTags=solutionRequest.titleTags,
#             newCauses=solutionRequest.newCauses,
#             downtime=solutionDowntime.solutionDowntime[solutionRequest.downtime] if solutionRequest.downtime in solutionDowntime.solutionDowntime  else "unknown",
#             shortTimeAction=solutionRequest.shortTimeAction,
#             longTimeAction=solutionRequest.shortTimeAction,
#             ressources=solutionRequest.ressources,
#             results=solutionRequest.results,
#             specifications=solutionRequest.specifications,
#             standards=solutionRequest.standards,
#             timestamp=datetime.datetime.now().isoformat(),
#             )
#         fault.save()
#         return fault
#     except Exception as e:
#         print(e)
#         raise HTTPException(detail=str(e),status_code=400)    

# @router.get("/{fault_id}",response_model=FaultSchema,status_code=200)
# def getPDCA(fault_id: str,db : Session = Depends(get_db)):
#     solution = db.query(FaultEvaluationModel).filter_by(id=fault_id).first()
#     return solution


# @router.get("",status_code=200)
# def getAllPDCA(db : Session = Depends(get_db)):
#     solutions = db.query(FaultEvaluationModel).all()
#     return solutions

#WICHTIG EINZUSTELEN! Es ein neues SolutionEvaluationModel, welches die Daten aus den PDCA Einträgen abspeichert und mit der Oberfläche kommuniziert

@router.post("/analyze",status_code=200)
def analyzeFault(faultSchema: FaultSchema,db : Session = Depends(get_db)):
    reason = int(faultSchema.reason)
    workplace = int(faultSchema.workplace)
    product = int(faultSchema.product)

    database = pd.read_csv('stoerungsauswertung.csv',delimiter=';')
    features = ['Fehlergrund', 'Arbeitsgang','Produkt']
    x = database[features]
    y = database['Maßnahme']
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x,y)
    pred = clf.predict([[reason,workplace,product]])

    X = database.iloc[:, [0,1]].values  
    y = database.iloc[:, 3].values
    classifier2 = KNeighborsClassifier(n_neighbors=6) 
    classifier2.fit(X,y)
    knn = classifier2.predict([[reason,workplace]])

    fault = db.query(FaultEvaluationModel).filter_by(id=faultSchema.id).first()
    fault.estimated_down_time = list(knn.tolist())[0]
    db.commit()

    return {
        "action": pred.tolist(),
        "downtime": knn.tolist()
    }
