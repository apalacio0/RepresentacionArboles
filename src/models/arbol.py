from __future__ import annotations
import json
import pyvista as pv

from models.rama import Rama
from models.fruto import estados

# Implementación de la clase Arbol

class Arbol:

    def __init__(self, data: dict, origen: tuple = (0, 0, 0)) -> None:
        """
        El único atributo que tiene un objeto de la clase Arbol va a ser
        su tronco, que es un objeto de la clase Rama
        """
        self.tronco: Rama = Rama.crear_rama_desde_json(origen = origen, data = data, rama_madre = None)
    
    def crear_arbol_desde_json(self, data: dict) -> Arbol:
        arbol = Arbol(data = data)
        return arbol
    
    def resumen_a_txt(self, txt_path: str) -> None:
        """
        Anota un resumen del árbol en un archivo .txt
        Después, anota también ese archivo la estructura del árbol, anotando
        de forma anidada un resumen de cada rama y cada fruto del árbol
        """
        with open(file = txt_path, mode = "w") as file:
            file.write("RESUMEN DEL ARBOL:\n")
            file.write("======================\n")
            file.write(f"- Numero de ramas:  {self.num_ramas()}.\n")
            file.write(f"- Numero de frutos: {self.num_frutos()}. De los cuales hay:\n")
            file.write(f"     {self.num_frutos_con_estado(estado = 2)} {estados[2]}.\n")
            file.write(f"     {self.num_frutos_con_estado(estado = 3)} {estados[3]}.\n")
            file.write(f"     {self.num_frutos_con_estado(estado = 4)} {estados[4]}.\n")
            file.write(f"- Volumen total de madera: {self.calcular_volumen():.2f}m^3.\n")
            file.write(f"- Volumen total de frutos: {self.calcular_volumen_frutos():.2f}m^3. De los cuales hay:\n")
            file.write(f"     {self.calcular_volumen_frutos_con_estado(estados = [0, 1]):.2f}m^3 de frutos todavia por madurar.\n")
            file.write(f"     {self.calcular_volumen_frutos_con_estado(estados = [2, 3]):.2f}m^3 de frutos dispuestos para consumo.\n")
            file.write(f"     {self.calcular_volumen_frutos_con_estado(estados = [4]):.2f}m^3 de frutos pasados.\n\n\n")

            file.write("ESTRUCTURA DEL ARBOL:\n")
            file.write("======================")
            self.tronco.resumen_a_txt(file = file, nivel = "")
    
    def dibujar_arbol(self, plotter: pv.Plotter) -> None:
        """
        Dibuja el árbol en el Plotter de entrada
        """
        self.tronco.dibujar_rama(plotter = plotter)

    def num_ramas(self) -> int:
        """
        Devuelve el número total de ramificaciones que tiene el árbol
        El tronco cuenta como una ramificación
        """
        num_ramas = self.tronco.num_ramas()
        return num_ramas
    
    def num_frutos(self) -> int:
        """
        Devuelve el número total de frutos que tiene el árbol
        """
        num_frutos = self.tronco.num_frutos()
        return num_frutos
    
    def num_frutos_con_estado(self, estado: int) -> int:
        """
        Devuelve el número total de frutos con estado de entrada que tiene el árbol
        """
        num_frutos_con_estado = self.tronco.num_frutos_con_estado(estado = estado)
        return num_frutos_con_estado

    
    def calcular_volumen(self) -> float:
        """
        Devuelve el volumen de todo el árbol
        """
        volumen = self.tronco.calcular_volumen()
        return volumen
    
    def calcular_volumen_frutos(self) -> float:
        """
        Devuelve el volumen total de frutos del árbol
        """
        volumen = self.tronco.calcular_volumen_frutos()
        return volumen
    
    def calcular_volumen_frutos_con_estado(self, estados: list[int]) -> float:
        """
        Devuelve el volumen total de frutos con estado de entrada del árbol
        """
        volumen = self.tronco.calcular_volumen_frutos_con_estado(estados = estados)
        return volumen
