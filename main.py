from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routers import faults
from routers import pdca

from sql_app.models import fault_evaluation_model
from sql_app.database import engine
from starlette.requests import Request
from starlette.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print(e)
        return Response(str(e), status_code=500)

app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS","GET","POST","PUT","DELETE"],
    allow_headers=["*"]
    )

fault_evaluation_model.BaseModel.metadata.create_all(bind=engine)

app.include_router(faults.router)
app.include_router(pdca.router)
