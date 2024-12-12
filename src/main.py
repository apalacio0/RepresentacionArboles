import pyvista as pv

from models.arbol import Arbol
from models.generadorJSONArbol import GeneradorJSONArbol
from constantes import *

# Inicialización del Plotter

plotter = pv.Plotter()
tierra = pv.Plane(center = (0, 0, 0), direction = (0, 0, 1), i_size = 100, j_size = 100)
plotter.add_mesh(mesh = tierra, color = "green", opacity = 1)

# Guardar un árbol creado

generadorArbol = GeneradorJSONArbol(max_niveles = 7)
generadorArbol.guardar_arbol(json_path = JSON_CREADO)

# Creación del árbol a partir del archivo de entrada

arbol = Arbol(json_path = JSON_CREADO)

# Dibujo del árbol en el Plotter

arbol.dibujar_arbol(plotter = plotter)

# Resumen del árbol en el archivo de salida

arbol.resumen_a_txt(txt_path = ARBOL_OUTPUT)

# Mostrar el dibujo del árbol

plotter.add_axes()
plotter.show()
