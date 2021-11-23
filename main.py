from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routers import faults
from sql_app.models import fault_evaluation_model
from sql_app.database import engine
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()


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


# conda create -n NAME
# conda activate NAME
# WIR BENUTZEN NICHT PIPENV SHELL WEGEN SKLEARN WIR INSTALLIEREN ALLES IN CONDA
# conda/pip install <ALL PACKAGES>