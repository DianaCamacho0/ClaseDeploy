from pydantic import BaseModel

class Diabetesdata(BaseModel):

    Pregnancies: int
    glucosa : int
    bloodpresure : int
    skinthickness: int
    insuline : int
    BMI : float
    diabetes : float
    age :int