import json
import random

def figuras_random():
    figuras = []
    nombres = ["cuadrado", "trianguloEquilatero", "circulo", "pentagono"]
                
    for i in range(0, random.randint(2, 10)):
        figuras.append({
            "nombre": nombres[random.randint(0, 3)],  # Cambié el rango a (0, 3)
            "x": random.randint(0, 400),
            "y": random.randint(0, 400),
            "medida": random.randint(0, 100)
        })
    return json.dumps(figuras)
