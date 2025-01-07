import json
import pyvista as pv

from models.arbol import Arbol
from constantes import *

class Campo:

    def __init__(self, json_path: str) -> None:
        self.arboles: list[Arbol] = self.crear_campo_desde_json(json_path = json_path)

    def crear_campo_desde_json(self, json_path: str) -> list[Arbol]:
        with open(file = json_path, mode = 'r') as file:
            data = json.load(file)
        arboles = []
        campo = data['campo']
        num_filas = campo['dimensiones']['filas']
        num_columnas = campo['dimensiones']['columnas']
        primer_origen_x = (-1) * SEPARACION_ARBOLES / 2 * (num_columnas - 1)
        primer_origen_y = (-1) * SEPARACION_ARBOLES / 2 * (num_filas - 1)
        for item in campo['filas']:
            fila = item['fila']
            num_fila = fila['num_fila'] - 1
            origen_y = primer_origen_y + SEPARACION_ARBOLES * num_fila
            for item in fila['arboles']:
                num_columna = item['num_columna'] - 1
                arbol_data = item['arbol']
                origen_x = primer_origen_x + SEPARACION_ARBOLES * num_columna
                origen = (origen_x, origen_y, 0)
                arbol = Arbol(data = arbol_data, origen = origen)
                arboles.append(arbol)
        return arboles
    
    def dibujar_campo(self, plotter: pv.Plotter):
        for arbol in self.arboles:
            arbol.dibujar_arbol(plotter = plotter)
