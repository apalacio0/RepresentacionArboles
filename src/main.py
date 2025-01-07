import pyvista as pv

from constantes import *
from models.campo import Campo
from models.generadorJSONCampo import GeneradorJSONCampo

# Inicialización del Plotter

plotter = pv.Plotter()
x_tierra = DIMENSIONES[1] * SEPARACION_ARBOLES
y_tierra = DIMENSIONES[0] * SEPARACION_ARBOLES
tierra = pv.Plane(center = (0, 0, 0), direction = (0, 0, 1), i_size = x_tierra, j_size = y_tierra)
plotter.add_mesh(mesh = tierra, color = "green", opacity = 1)

# Generar y guardar un campo creado

generadorCampo = GeneradorJSONCampo(dimensiones = DIMENSIONES)
generadorCampo.guardar_campo(JSON_CREADO)

# Creación del campo a partir del archivo JSON creado

campo = Campo(json_path = JSON_CREADO)

# Dibujo del campo en el Plotter

campo.dibujar_campo(plotter = plotter)

"""# Resumen del árbol en el archivo de salida

arbol.resumen_a_txt(txt_path = ARBOL_OUTPUT)"""

# Mostrar el dibujo del árbol

plotter.add_axes()
plotter.show()
