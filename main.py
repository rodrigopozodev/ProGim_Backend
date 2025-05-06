import os
from fastapi import FastAPI
from pydantic import BaseModel
from models.generador_rutinas import generar_rutina
from api.endpoints import generar_rutina_api

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

@app.post("/generar-rutina")
async def generar_rutina_api(usuario: Usuario):
    # Convertimos el objeto 'usuario' en un diccionario
    usuario_dict = usuario.dict()
    
    # Generamos la rutina personalizada
    rutina = generar_rutina(usuario_dict)
    
    return rutina

# Configuración para que Uvicorn escuche en el puerto correcto
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto que Render proporciona
    uvicorn.run(app, host="0.0.0.0", port=port)
