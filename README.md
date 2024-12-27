# Iris Classification API

Esta es una API que utiliza un modelo de clasificación para predecir las especies de flores Iris en base a sus características.

## Requisitos
- Python 3.8  or newer
- Docker

## Instrucciones seguir paso a paso

### 1. Entrenar el modelo
Ejecuta el script `train_model.py` para entrenar y guardar el modelo:
```
python train_model.py 
```

### 2. Contenerización con Docker
Ejecutar el siguiente comando para construir la imagen
```
docker build -t iris-api . 
```

luego ejecutar el siguiente comando para ejecutar el contenedor
```
docker run -d -p 5000:5000 iris-api
```
### 3. Comprobación de la API
Una vez que los contenedores estén en ejecución, puedes acceder a la API de FastAPI en la siguiente URL:
```
http://localhost:5000
```
La documentación interactiva(Swagger) de la API estará disponible en:
```
http://localhost:5000/docs
```

¡Listo! Ya puedes usar y probar la aplicación. 🎉



