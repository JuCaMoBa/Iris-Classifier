from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
import pickle

def train_and_save_model():
    # Cargar los datos iris
    iris = load_iris()
    X, y = iris.data, iris.target

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo de clasificación
    model = DecisionTreeClassifier(random_state=42, max_depth=4)
    model.fit(X_train, y_train)

    # Agregar los nombres de las clases al modelo
    model.class_names = iris.target_names

    #Prediccion
    y_pred = model.predict(X_test)

    #precision del modelo
    precision = precision_score(y_test, y_pred, average='weighted')
    print(f"Precision del modelo: {precision}")

    # Guardar el modelo entrenado en un archivo
    with open('model/model_iris.pkl', 'wb') as file:
        pickle.dump(model, file)
    print("Modelo entrenado y guardado correctamente")

if __name__ == "__main__":
    train_and_save_model()




