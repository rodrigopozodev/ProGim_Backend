from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from models.generador_rutinas import generar_rutina

# Configuración de la app FastAPI
app = FastAPI()

# Habilitar CORS para permitir que el frontend acceda al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los dominios (puedes especificar los dominios si lo deseas)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

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
    usuario_dict = usuario.dict()
    rutina = generar_rutina(usuario_dict)
    
    return rutina

# Configuración para que Uvicorn escuche en el puerto correcto
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Usa el puerto que Render proporciona
    uvicorn.run(app, host="0.0.0.0", port=port)
