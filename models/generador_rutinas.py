# Lógica del generador de rutinas
import random

# Base de datos de ejercicios (esto se puede expandir o importar desde un CSV)
ejercicios = {
    "sentadillas": {"grupo_muscular": "piernas", "nivel": "principiante", "material": ["barra"], "calorias": 30},
    "press_banca": {"grupo_muscular": "pecho", "nivel": "principiante", "material": ["barra"], "calorias": 40},
    "dominadas": {"grupo_muscular": "espalda", "nivel": "intermedio", "material": ["barra"], "calorias": 50},
    "curl_biceps": {"grupo_muscular": "brazos", "nivel": "principiante", "material": ["mancuernas"], "calorias": 20},
    "peso_muerto": {"grupo_muscular": "piernas", "nivel": "intermedio", "material": ["barra"], "calorias": 60},
}

def generar_rutina(usuario):
    rutina = {}
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

    # Filtrar ejercicios según el perfil del usuario
    ejercicios_filtrados = [ej for ej, data in ejercicios.items()
                            if data["nivel"] == usuario["nivel"] and 
                               all(item in usuario["material"] for item in data["material"])]

    for dia in dias[:usuario["dias_disponibles"]]:
        rutina[dia] = []
        for _ in range(3):  # Tres ejercicios por día
            ejercicio = random.choice(ejercicios_filtrados)
            rutina[dia].append({
                "ejercicio": ejercicio,
                "grupo_muscular": ejercicios[ejercicio]["grupo_muscular"],
                "nivel": ejercicios[ejercicio]["nivel"],
                "material": ejercicios[ejercicio]["material"],
                "calorias_estimadas": ejercicios[ejercicio]["calorias"]
            })
    
    return rutina
