from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from models.generador_rutinas import generar_rutina
import auth  # Import the auth module

# Configuración de la app FastAPI
app = FastAPI()

# Habilitar CORS para permitir que el frontend acceda al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origen del frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluir el router de autenticación
app.include_router(auth.router, tags=["authentication"])

# Punto de entrada para verificar que el servidor está funcionando
@app.get("/")
async def root():
    return {"message": "API de GIM funcionando correctamente"}

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