import json

from models.generadorJSONArbol import GeneradorJSONArbol
from constantes import *


class GeneradorJSONCampo:

    def __init__(self, dimensiones: tuple = DIMENSIONES) -> None:
        self.campo: dict = self.generar_campo(dimensiones = dimensiones)

    def generar_campo(self, dimensiones: tuple) -> dict:
        generadorJSONArbol = GeneradorJSONArbol(max_niveles = MAX_NIVELES)
        filas = dimensiones[0]
        columnas = dimensiones[1]

        campo = {
            "campo": {
                "dimensiones": {
                    "filas": filas,
                    "columnas": columnas
                },
                "filas": [
                    {
                        "fila": {
                            "num_fila": num_fila + 1,
                            "arboles": [
                                {
                                    "num_columna": num_columna + 1,
                                    "arbol": generadorJSONArbol.generar_arbol(max_niveles = MAX_NIVELES)
                                } for num_columna in range(columnas)
                            ]
                        }
                        
                    } for num_fila in range(filas)
                ]
            } 
        }
        return campo
    
    def guardar_campo(self, json_path: str) -> None:
        with open(json_path, "w") as file:
            json.dump(self.campo, file, indent = 4)
        