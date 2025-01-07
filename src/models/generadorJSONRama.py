import math
import random

from constantes import *
from models.generadorJSONFruto import GeneradorJSONFruto

class GeneradorJSONRama:

    def __init__(self, nivel: int = 0, max_niveles: int = MAX_NIVELES,
                 longitud_rama_madre: float = 0.0, grosor_rama_madre: float = 0.0) -> None:
        self.rama: dict = self.generar_rama(nivel = nivel, max_niveles = max_niveles, longitud_rama_madre = longitud_rama_madre, grosor_rama_madre = grosor_rama_madre)
    
    def generar_rama(self, nivel: int = 0, max_niveles: int = MAX_NIVELES,
                     longitud_rama_madre: float = 0.0, grosor_rama_madre: float = 0.0) -> dict:
        if nivel >= max_niveles:
            return None
        
        datos = (self.datos_tronco() if nivel == 0
                 else self.datos_rama(longitud_rama_madre = longitud_rama_madre, grosor_rama_madre = grosor_rama_madre))
        
        generadorJSONFruto = GeneradorJSONFruto()

        rama = {
            "longitud": datos["longitud"],
            "grosor": datos["grosor"],
            "altura_rama_madre": datos["altura_rama_madre"],
            "phi": datos["phi"],
            "theta": datos["theta"],
            "ramas_hijas": [
                self.generar_rama(
                    nivel = nivel + 1,
                    max_niveles = MAX_NIVELES,
                    longitud_rama_madre = datos["longitud"],
                    grosor_rama_madre = datos["grosor"]
                ) for _ in range(datos["num_ramas_hijas"])
            ],
            "frutos": [
                generadorJSONFruto.generar_fruto() for _ in range(datos["num_frutos"])
            ]
        }
        rama["ramas_hijas"] = [rama_hija for rama_hija in rama["ramas_hijas"] if rama_hija is not None]   # filtrar las ramas hijas que son None
        rama["ramas_hijas"].sort(key = lambda rama_hija: rama_hija["altura_rama_madre"])   # ordenar las ramas hijas por la altura a la que salen
        rama["frutos"].sort(key = lambda fruto: fruto["altura_rama"])   # ordenar los frutos por la altura a la que salen
        return rama
    
    def datos_tronco(self) -> dict:
        longitud = round(random.uniform(MIN_LONGITUD_TRONCO, MAX_LONGITUD_RAMA), 2)   # mejorar
        grosor = round(random.uniform(MIN_GROSOR_TRONCO, MAX_GROSOR_TRONCO), 2)
        altura_rama_madre = 0.0
        phi = 0.0
        theta = 0.0
        num_ramas_hijas = self.calcular_num_ramas_hijas(longitud = longitud)
        num_frutos = 0
        
        return {
            "longitud": longitud,
            "grosor": grosor,
            "altura_rama_madre": altura_rama_madre,
            "phi": phi,
            "theta": theta,
            "num_ramas_hijas": num_ramas_hijas,
            "num_frutos": num_frutos
        }
    
    def datos_rama(self, longitud_rama_madre: float, grosor_rama_madre:float) -> dict:
        longitud = round(random.uniform(longitud_rama_madre * 0.3, longitud_rama_madre * 0.8), 2)
        grosor = round(random.uniform(grosor_rama_madre * 0.5, grosor_rama_madre * 0.8), 2)
        altura_rama_madre = round(random.uniform(0.0, 1.0), 2)
        phi = round(random.uniform(0.0, 360.0), 2)
        theta = round(random.uniform(25.0, 70.0), 2)
        num_ramas_hijas = self.calcular_num_ramas_hijas(longitud = longitud)
        num_frutos = self.calcular_num_frutos(longitud = longitud)
        
        return {
            "longitud": longitud,
            "grosor": grosor,
            "altura_rama_madre": altura_rama_madre,
            "phi": phi,
            "theta": theta,
            "num_ramas_hijas": num_ramas_hijas,
            "num_frutos": num_frutos
        }
    
    def calcular_num_ramas_hijas(self, longitud: float) -> int:
        escala = 5
        media = longitud / MAX_LONGITUD_RAMA * escala
        desviacion = 1
        ramas_hijas_propuestas = random.gauss(mu = media, sigma = desviacion)
        num_ramas_hijas = max(0, math.trunc(ramas_hijas_propuestas))
        return num_ramas_hijas
    
    def calcular_num_frutos(self, longitud: float) -> int:
        escala = 4
        media = longitud / MAX_LONGITUD_RAMA * escala
        desviacion = 1
        frutos_propuestos = random.gauss(mu = media, sigma = desviacion)
        num_frutos = max(0, math.trunc(frutos_propuestos))
        return num_frutos
    