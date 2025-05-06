# Endpoints de FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Modelo de entrada
class Usuario(BaseModel):
    edad: int
    sexo: str
    peso: float
    estatura: float
    objetivo: str
    nivel: str
    dias_disponibles: int
    tiempo_diario: int
    lesiones: list
    material: list
    dieta: str

# Ejemplo de ejercicios predefinidos (esto se puede expandir desde el CSV)
ejercicios = {
    "sentadillas": {"grupo_muscular": "piernas", "nivel": "principiante", "material": ["barra"], "calorias": 30},
    "press_banca": {"grupo_muscular": "pecho", "nivel": "principiante", "material": ["barra"], "calorias": 40},
    "dominadas": {"grupo_muscular": "espalda", "nivel": "intermedio", "material": ["barra"], "calorias": 50},
}

# Generación de rutina básica
@app.post("/generar-rutina")
async def generar_rutina(usuario: Usuario):
    rutina = {}
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

    for dia in dias[:usuario.dias_disponibles]:
        rutina[dia] = []
        for _ in range(3):  # Tres ejercicios por día
            ejercicio = random.choice(list(ejercicios.keys()))
            rutina[dia].append({
                "ejercicio": ejercicio,
                "grupo_muscular": ejercicios[ejercicio]["grupo_muscular"],
                "nivel": ejercicios[ejercicio]["nivel"],
                "material": ejercicios[ejercicio]["material"],
                "calorias_estimadas": ejercicios[ejercicio]["calorias"]
            })
    
    return rutina
