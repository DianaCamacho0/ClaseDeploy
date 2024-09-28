from fastapi import FastAPI
from asignatura import asignatura
from routers import routerDiabetes

app = FastAPI()

app.include_router(routerDiabetes.router)

