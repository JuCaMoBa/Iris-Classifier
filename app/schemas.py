from pydantic import BaseModel


class IrisOutputData(BaseModel):
    sepalo_longitud: float
    sepalo_ancho: float
    petalo_longitud: float
    petalo_ancho: float
    iris_class: str

class IrisInputData(BaseModel):
    sepalo_longitud: float
    sepalo_ancho: float
    petalo_longitud: float
    petalo_ancho: float

