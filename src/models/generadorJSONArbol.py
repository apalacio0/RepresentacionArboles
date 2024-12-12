import json
import random
import math

from models.arbol import Arbol
from constantes import *
 
class GeneradorJSONArbol:

    def __init__(self, max_niveles: int = MAX_NIVELES) -> Arbol:
        self.arbol = self.generar_arbol(max_niveles = max_niveles)

    def guardar_arbol(self, json_path: str) -> None:
        with open(json_path, "w") as file:
            json.dump(self.arbol, file, indent = 4)

    def generar_fruto(self) -> dict:
        return {
            "tamano": round(random.uniform(0.2, 0.5), 2),
            "estado": random.randint(0, 4),
            "altura_rama": round(random.uniform(0.0, 1.0), 2)
        }
    
    def generar_rama(self, nivel: int = 0, max_niveles: int = MAX_NIVELES,
                     longitud_rama_madre: float = 0.0, grosor_rama_madre: float = 0.0) -> dict:
        if nivel >= max_niveles:
            return None
        
        if nivel == 0:
            datos = self.datos_tronco()
        else:
            datos = self.datos_rama(longitud_rama_madre = longitud_rama_madre, grosor_rama_madre = grosor_rama_madre)

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
                self.generar_fruto() for _ in range(datos["num_frutos"])
            ]
        }
        rama["ramas_hijas"] = [rama_hija for rama_hija in rama["ramas_hijas"] if rama_hija is not None]   # filtrar las ramas hijas que son None
        return rama
    
    def generar_arbol(self, max_niveles: int = MAX_NIVELES) -> dict:
        arbol_dict = self.generar_rama(nivel = 0, max_niveles = max_niveles, longitud_rama_madre = 0, grosor_rama_madre = 0)
        return arbol_dict
    
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
        theta = round(random.uniform(25.0, 90.0), 2)
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
        max_ramas_hijas = math.trunc(longitud / MAX_LONGITUD_RAMA * 4)
        num_ramas = random.randint(0, max_ramas_hijas)
        return num_ramas
    
    def calcular_num_frutos(self, longitud: float) -> int:
        max_frutos = math.trunc(longitud / MAX_FRUTOS * 4)
        num_frutos = random.randint(0, max_frutos)
        return num_frutos
