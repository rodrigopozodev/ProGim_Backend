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
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    grupos_musculares = ["piernas", "pecho", "espalda", "brazos"]
    
    # Filtrar ejercicios que coincidan con nivel y material
    ejercicios_filtrados = {
        grupo: [
            nombre for nombre, data in ejercicios.items()
            if data["grupo_muscular"] == grupo
            and data["nivel"] == usuario["nivel"]
            and all(item in usuario["material"] for item in data["material"])
        ]
        for grupo in grupos_musculares
    }

    for i in range(usuario["dias_disponibles"]):
        dia = dias_semana[i]
        grupo = grupos_musculares[i % len(grupos_musculares)]
        posibles_ejercicios = ejercicios_filtrados.get(grupo, [])
        
        if not posibles_ejercicios:
            rutina[dia] = [{"mensaje": f"No hay ejercicios disponibles para {grupo} con tu material"}]
            continue
        
        # Evita duplicados y limita a 3 ejercicios como máximo
        seleccionados = random.sample(posibles_ejercicios, k=min(3, len(posibles_ejercicios)))
        
        rutina[dia] = [{
            "ejercicio": nombre,
            "grupo_muscular": ejercicios[nombre]["grupo_muscular"],
            "nivel": ejercicios[nombre]["nivel"],
            "material": ejercicios[nombre]["material"],
            "calorias_estimadas": ejercicios[nombre]["calorias"]
        } for nombre in seleccionados]

    return rutina
