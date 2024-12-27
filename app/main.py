from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="API", version="1.0.0")

#rutas
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API"}


