import json
from models.rama import Rama
import pyvista as pv

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
            file.write(f"- Numero de frutos: {self.num_frutos()}.\n\n\n")

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
        return self.tronco.num_ramas()
    
    def num_frutos(self) -> int:
        """
        Devuelve el número total de frutos que tiene el árbol
        """
        return self.tronco.num_frutos()
