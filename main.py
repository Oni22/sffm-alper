from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routers import test
from sql_app.models import fault_evaluation_model
from sql_app.database import engine
from sklearn.model_selection import KFold
import csv 

app = FastAPI()


def toCSV(file):
    with open(file, newline='',encoding='utf-8-sig') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        data = {}
        for row in spamreader:
            key = row[0]
            value = row[1]
            data[key] = value
        pyFile = open("products.py","x")
        pyFile.write(str(data))
        pyFile.close()

toCSV("zProdukt.csv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS","GET","POST","PUT","DELETE"],
    allow_headers=["*"]
    )

fault_evaluation_model.BaseModel.metadata.create_all(bind=engine)

app.include_router(test.router)


# conda create -n NAME
# conda activate NAME
# WIR BENUTZEN NICHT PIPENV SHELL WEGEN SKLEARN WIR INSTALLIEREN ALLES IN CONDA
# conda/pip install <ALL PACKAGES>