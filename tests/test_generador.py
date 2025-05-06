# Pruebas unitarias para el generador
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generar_rutina():
    response = client.post("/generar-rutina", json={
        "edad": 25,
        "sexo": "masculino",
        "peso": 80,
        "estatura": 179,
        "objetivo": "perder_grasa",
        "nivel": "principiante",
        "dias_disponibles": 3,
        "tiempo_diario": 60,
        "lesiones": [],
        "material": ["barra"],
        "dieta": "balanceada"
    })
    assert response.status_code == 200
    assert "lunes" in response.json()
    assert "ejercicio" in response.json()["lunes"][0]

def test_generar_dieta():
    response = client.post("/generar-dieta", json={
        "edad": 25,
        "sexo": "masculino",
        "peso": 80,
        "estatura": 179,
        "objetivo": "perder_grasa",
        "nivel": "principiante",
        "dias_disponibles": 3,
        "tiempo_diario": 60,
        "lesiones": [],
        "material": ["barra"],
        "dieta": "balanceada"
    })
    assert response.status_code == 200
    assert "calorias_totales" in response.json()
