from __future__ import annotations
from typing import TextIO
import pyvista as pv

# Diccionarios

estados = {
    0: "Recien nacido",
    1: "Creciendo",
    2: "Para coger",
    3: "Maduro",
    4: "Pasado"
}

colores = {
    0: [50, 185, 0],
    1: [210, 250, 50],
    2: [255, 185, 0],
    3: [255, 0, 0],
    4: [135, 85, 0]
}

# Implementación de la clase Fruto

class Fruto:

    def __init__(self, tamano: float, estado: int, rama: 'Rama', altura_rama: float) -> None: # type: ignore
        """
        Estados: {0: recien nacido, 1: creciendo, 2: para coger, 3: maduro, 4: pasado}
        altura_rama es el punto de la rama en el que aparece el fruto (0, 1]
        """
        self.tamano: float = tamano
        self.estado: int = estado
        self.posicion: tuple = self.calcular_posicion(rama = rama, altura_rama = altura_rama)
    
    @staticmethod
    def crear_fruto_desde_json(data: dict, rama: 'Rama') -> Fruto: # type: ignore
        """
        Crea un fruto descrito en un archivo .json
        Devuelve ese fruto
        """
        fruto = Fruto(
            tamano = data['tamano'],
            estado = data['estado'],
            rama = rama,
            altura_rama = data['altura_rama']
        )

        return fruto
    
    def resumen_a_txt(self, file: TextIO, nivel: str):
        """
        Anota un resumen del fruto en un archivo .txt
        """
        file.write(f"{nivel}     - Fruto -> Tamano: {self.tamano * 100}cm. Estado: {estados[self.estado]}.\n")
    
    def dibujar_fruto(self, plotter: pv.Plotter) -> None:
        """
        Dibuja el fruto en el Plotter de entrada
        """
        radio = self.tamano
        fruto = pv.Sphere(radius = radio, center = self.posicion)
        color = colores[self.estado]
        plotter.add_mesh(fruto, color = color, opacity = 1)

    def calcular_posicion(self, rama: 'Rama', altura_rama: float) -> tuple: # type: ignore
        """
        Calcula la posición exacta en un mapa 3D en la que se encuentra el fruto
        Devuelve esa posición
        """
        factor = rama.longitud * altura_rama
        posicion = tuple(ori + dir * factor for ori, dir in zip(rama.origen, rama.direccion))
        return posicion