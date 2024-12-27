from fastapi import APIRouter, HTTPException
from app.schemas import IrisInputData, IrisOutputData
from services.iris_classifier import IrisClassifier


# Crear el router
router = APIRouter()


@router.post("/iris-classifier", response_model=IrisOutputData)
def get_iris_class(data: IrisInputData):
    try:
        iris_classifier = IrisClassifier()
        iris_class = iris_classifier.predict(data)
        return IrisOutputData(iris_class=iris_class, **data.model_dump())
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {str(e)}")

