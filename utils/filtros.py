# Funciones de filtrado y validación
# Filtros para el generador de rutinas

def filtrar_por_material(ejercicios, materiales_disponibles):
    """Filtra los ejercicios según los materiales disponibles del usuario"""
    return [ej for ej, data in ejercicios.items() if all(item in materiales_disponibles for item in data["material"])]

def filtrar_por_nivel(ejercicios, nivel_usuario):
    """Filtra los ejercicios según el nivel del usuario"""
    return [ej for ej, data in ejercicios.items() if data["nivel"] == nivel_usuario]

def filtrar_por_lesiones(ejercicios, lesiones_usuario):
    """Filtra los ejercicios que no son recomendados según las lesiones del usuario"""
    # Asumimos que en cada ejercicio se especifican posibles contraindicaciones
    return [ej for ej, data in ejercicios.items() if not any(lesion in data.get("contraindicaciones", []) for lesion in lesiones_usuario)]
