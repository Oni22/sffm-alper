from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routers import test
from sql_app.models import fault_evaluation_model
from sql_app.database import engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS","GET","POST","PUT","DELETE"],
    allow_headers=["*"]
    )

fault_evaluation_model.BaseModel.metadata.create_all(bind=engine)

app.include_router(test.router)