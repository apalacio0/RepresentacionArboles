import json
import pyvista as pv

from models.rama import Rama
from models.fruto import estados

# Implementación de la clase Arbol

class Arbol:

    def __init__(self, json_path: str) -> None:
        """
        El único atributo que tiene un objeto de la clase Arbol va a ser
        su tronco, que es un objeto de la clase Rama
        """
        self.tronco: Rama = self.crear_arbol_desde_json(json_path = json_path)
    
    def crear_arbol_desde_json(self, json_path: str) -> Rama:
            """
            Crea un árbol descrito en un archivo .json creando una rama que entiende
            como tronco del árbol
            Devuelve esa Rama
            """
            with open(file = json_path, mode = 'r') as file:
                data = json.load(file)
            tronco = Rama.crear_rama_desde_json(data = data)
            return tronco
    
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
            file.write(f"     {self.num_frutos_con_estado(2)} {estados[2]}, {self.num_frutos_con_estado(3)} {estados[3]} y {self.num_frutos_con_estado(4)} {estados[4]}.\n")
            file.write(f"- Volumen total: {self.calcular_volumen():.2f}m^3.\n\n\n")

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
