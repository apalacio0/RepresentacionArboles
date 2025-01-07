import random

class GeneradorJSONFruto:

    def __init__(self) -> None:
        self.fruto = self.generar_fruto()
    
    def generar_fruto(self) -> dict:
        return {
            "tamano": round(random.uniform(0.2, 0.5), 2),
            "estado": random.randint(0, 4),
            "altura_rama": round(random.uniform(0.0, 1.0), 2)
        }