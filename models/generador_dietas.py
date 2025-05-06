def calcular_calorias_totales(usuario):
    # Fórmula simplificada para calcular el TDEE (Total Daily Energy Expenditure)
    if usuario['sexo'] == 'masculino':
        tmb = 10 * usuario['peso'] + 6.25 * usuario['estatura'] - 5 * usuario['edad'] + 5
    else:
        tmb = 10 * usuario['peso'] + 6.25 * usuario['estatura'] - 5 * usuario['edad'] - 161

    tdee = tmb * 1.55  # Consideramos un nivel de actividad moderado
    return tdee

def generar_dieta(usuario):
    calorias_totales = calcular_calorias_totales(usuario)

    # Aquí puedes crear un reparto de macros basado en el objetivo
    if usuario['objetivo'] == 'perder_grasa':
        calorias_totales -= 500  # Déficit calórico

    # Crear una dieta simplificada
    dieta = {
        "calorias_totales": calorias_totales,
        "proteinas": calorias_totales * 0.3 / 4,  # 30% de las calorías en proteínas
        "grasas": calorias_totales * 0.25 / 9,   # 25% en grasas
        "carbohidratos": calorias_totales * 0.45 / 4  # 45% en carbohidratos
    }

    # Ejemplo de alimentos sugeridos
    alimentos = ["pollo", "arroz", "aguacate", "pasta", "frutas", "verduras"]

    return {"dieta": dieta, "alimentos_sugeridos": alimentos}
