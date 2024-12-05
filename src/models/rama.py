from __future__ import annotations
import math
from typing import TextIO
import numpy as np
import pyvista as pv

from models.fruto import Fruto

# Implementación de la clase Rama

class Rama:
    
    def __init__(self, longitud: float, grosor:float, rama_madre: Rama = None,
                 altura_rama_madre: float = 0, phi: float = 0, theta: float = 0) -> None:
        """
        altura_rama_madre es el punto de la rama madre en el que aparece la rama (0, 1]
        phi es el ángulo de rotación respecto al eje Z [0, 2*pi)
        theta es el ángulo de rotación respecto al eje X [0, 2*pi)
        """
        self.longitud: float = longitud
        self.grosor: float = grosor
        self.rama_madre: Rama = rama_madre
        self.origen: tuple = self.calcular_origen(altura_rama_madre = altura_rama_madre)
        self.direccion: tuple = self.calcular_direccion(math.radians(phi), math.radians(theta))
        factor = self.longitud / 2
        self.centro: tuple = tuple(ori + dir * factor for ori, dir in zip(self.origen, self.direccion))
        self.ramas_hijas: list[Rama] = []
        self.frutos: list[Fruto] = []
    
    @staticmethod
    def crear_rama_desde_json(data: dict, rama_madre: Rama = None) -> Rama:
        """
        Crea una rama descrita en un archivo .json, junto con sus frutos y sus subramas
        Devuelve esa rama
        """        
        rama = Rama(
            longitud = data['longitud'],
            grosor = data['grosor'],
            rama_madre = rama_madre,
            altura_rama_madre = data['altura_rama_madre'],
            phi = data['phi'],
            theta = data['theta']
        )

        for fruto_data in data['frutos']:
            fruto = Fruto.crear_fruto_desde_json(data = fruto_data, rama = rama)
            rama.add_fruto(fruto = fruto)

        for rama_hija_data in data['ramas_hijas']:
            rama_hija = Rama.crear_rama_desde_json(rama_hija_data, rama_madre = rama)
            rama.add_rama_hija(rama_hija)
        
        return rama
    
    def resumen_a_txt(self, file: TextIO, nivel: str):
        """
        Anota un resumen de la rama en un archivo .txt
        Iterativamente, hace lo mismo con sus frutos y sus subramas
        """
        file.write(f"\n{nivel}- Rama -> Longitud: {self.longitud}m. Radio: {self.grosor}m.\n")
        for fruto in self.frutos:
            fruto.resumen_a_txt(file = file, nivel = nivel)
        for rama_hija in self.ramas_hijas:
            rama_hija.resumen_a_txt(file = file, nivel = nivel + "     ")

    def dibujar_rama(self, plotter: pv.Plotter) -> None:
            """
            Dibuja la rama en el Plotter de entrada
            Iterativamente, hace lo mismo con sus frutos y sus subramas
            """
            rama = pv.Cylinder(center = self.centro, direction = self.direccion, radius = self.grosor, height = self.longitud)
            plotter.add_mesh(rama, color = "brown", opacity = 1)

            for fruto in self.frutos:
                fruto.dibujar_fruto(plotter = plotter)

            for rama_hija in self.ramas_hijas:
                rama_hija.dibujar_rama(plotter = plotter)
    
    def calcular_origen(self, altura_rama_madre: float) -> tuple:
        """
        Calcula la posición exacta en un mapa 3D en la que se encuentra la base de la rama
        Si la rama no tiene rama madre, entiende que es el tronco del árbol y lo situa en (0, 0, 0)
        Devuelve esa posición
        """
        if self.rama_madre is None:
            return (0, 0, 0)
        else:
            factor = self.rama_madre.longitud * altura_rama_madre
            origen = tuple(ori + dir * factor for ori, dir in zip(self.rama_madre.origen, self.rama_madre.direccion))
            return origen
    
    def calcular_direccion(self, phi: float, theta: float) -> tuple:
        """
        Calcula una tupla unitaria que apunta en la dirección y el sentido en que crece la rama
        Devuelve esa tupla
        """
        x = np.cos(phi) * np.sin(theta)
        y = np.sin(phi) * np.sin(theta)
        z = np.cos(theta)
        direccion = (x, y, z)
        return direccion
    
    def add_rama_hija(self, rama_hija: Rama) -> None:
        """
        Añade una rama hija a la rama
        """
        self.ramas_hijas.append(rama_hija)

    def add_fruto(self, fruto: Fruto) -> None:
        """
        Añade un fruto a la rama
        """
        self.frutos.append(fruto)
    
    def num_ramas(self) -> int:
        """
        Devuelve el número total de ramificaciones que existen a partir de la rama
        La propia rama cuenta como una ramificación
        """
        num_ramas = 0
        if len(self.ramas_hijas) == 0:
            return 1
        else:
            for rama_hija in self.ramas_hijas:
                num_ramas += rama_hija.num_ramas()
            return num_ramas + 1
    
    def num_frutos(self) -> int:
        """
        Devuelve el número total de frutos que hay en la rama
        o en una de sus ramificaciones
        """
        num_frutos = len(self.frutos)
        for rama_hija in self.ramas_hijas:
            num_frutos += rama_hija.num_frutos()
        return num_frutos
