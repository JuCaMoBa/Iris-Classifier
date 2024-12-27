import numpy as np
import pickle
from app.schemas import IrisInputData

def load_model():
    # Cargar el modelo entrenado 
    with open('model/model_iris.pkl', 'rb') as file:
        return  pickle.load(file)
    
class IrisClassifier:
    def __init__(self):
        self.model = load_model()

    def predict(self, iris_data: IrisInputData):
        features = np.array([iris_data.sepalo_longitud, iris_data.sepalo_ancho, iris_data.petalo_longitud, iris_data.petalo_ancho]).reshape(1, -1)
        prediction = self.model.predict(features)
        return self.model.class_names[int(prediction[0])]
        

    