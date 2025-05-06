# 🏋️‍♂️ AI Gym Routine Generator

Este proyecto es un backend con inteligencia artificial desarrollado en Python que genera rutinas de entrenamiento de gimnasio personalizadas, basadas en características individuales como edad, sexo, estatura, peso, tiempo disponible, lesiones, nivel, objetivo y más.

---

## 🚀 Objetivo del Proyecto

Desarrollar una IA capaz de crear **rutinas óptimas y seguras** para usuarios de todo tipo, considerando:

- Perfil físico (edad, sexo, peso, estatura)
- Nivel y experiencia
- Objetivo (pérdida de grasa, ganancia muscular, mantenimiento)
- Lesiones o limitaciones
- Equipamiento disponible
- Dieta y tiempo diario/semanal
- Progreso registrado a lo largo del tiempo

---

## 🧠 Fases del Desarrollo

### 1. Definición y Planificación

- Inputs esperados del usuario
- Outputs detallados por día
- Base de ejercicios y metadatos
- Decisión entre reglas programadas, machine learning o IA generativa

### 2. Estructura del Proyecto

rutina_ai/
├── main.py # Punto de entrada principal
├── models/
│ └── generador_rutinas.py # Lógica de generación personalizada
├── data/
│ └── ejercicios.csv # Base de datos de ejercicios
├── utils/
│ └── filtros.py # Funciones de filtrado y validación
├── api/
│ └── endpoints.py # Endpoints FastAPI
├── tests/
│ └── test_generador.py # Pruebas unitarias
├── requirements.txt
└── README.md

### 3. Base de Datos de Ejercicios

- Archivo `.csv` o `.json` con:
  - Nombre
  - Grupo muscular
  - Nivel recomendado
  - Material necesario
  - Tipo (compuesto/aislado)
  - Contraindicaciones (por lesión)
  - Calorías estimadas

### 4. Generador de Rutinas

- Opción 1: Reglas programadas
  - Distribución de días
  - Filtros por perfil
  - Generación de rutina equilibrada
- Opción 2: Machine Learning (versión avanzada)
  - Dataset con usuarios y rutinas eficaces
  - Clasificadores o modelos de recomendación
  - Aprendizaje continuo

### 5. Ajuste Automático por Progreso

- Endpoint para registrar avances
- Adaptación de la rutina (peso, reps, deload, etc.)
- Registro de feedback del usuario

### 6. API REST

- Framework: FastAPI
- Endpoint: `POST /generar-rutina`
- Entrada: JSON con los datos del usuario
- Salida: JSON con rutina detallada por día

### 7. Testing

- Pruebas unitarias con Pytest
- Casos extremos y validaciones
- Simulación de perfiles variados

### 8. Futuras Mejoras

- Aprendizaje automático del comportamiento de usuarios
- Integración con dispositivos fitness (smartwatches, básculas)
- Generación de dietas sincronizadas
- Exportación a PDF/Excel
- Dashboard visual con progreso y estadísticas

---

## 🧰 Tecnologías Usadas

| Función                  | Herramienta                   |
| ------------------------ | ----------------------------- |
| Backend API              | FastAPI                       |
| Lógica IA                | Python, Scikit-learn, Pandas  |
| Formato datos            | JSON, CSV                     |
| Base de datos ejercicios | Propia en `data/`             |
| Testing                  | Pytest                        |
| Documentación API        | Swagger (incluido en FastAPI) |

---

## ⚙️ Instalación y Ejecución

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/rutina_ai.git
cd rutina_ai
```

2. Crea un entorno virtual:

python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

3. Instala las dependencias:

pip install -r requirements.txt

4. Ejecuta el servidor:

uvicorn main:app --reload

5. Accede a la documentación interactiva en:

http://localhost:8000/docs

📤 Ejemplo de Petición
Endpoint: POST /generar-rutina

{
"edad": 25,
"sexo": "masculino",
"peso": 80,
"estatura": 179,
"objetivo": "hipertrofia",
"nivel": "principiante",
"dias_disponibles": 4,
"tiempo_diario": 60,
"lesiones": ["lumbalgia"],
"material": ["mancuernas", "barra", "máquinas"],
"dieta": "hipercalórica"
}
