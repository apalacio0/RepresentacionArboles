import pyvista as pv

from models.arbol import Arbol

# Nombre de los archivos de entrada y salida

ARBOL_INPUT = 'input_output/inputs/arbol.json'
ARBOL_OUTPUT = 'input_output/outputs/arbol.txt'

# Inicialización del Plotter

plotter = pv.Plotter()
tierra = pv.Plane(center = (0, 0, 0), direction = (0, 0, 1), i_size = 100, j_size = 100)
plotter.add_mesh(mesh = tierra, color = "green", opacity = 1)

# Creación del árbol a partir del archivo de entrada

arbol = Arbol(json_path = ARBOL_INPUT)

# Dibujo del árbol en el Plotter

arbol.dibujar_arbol(plotter = plotter)

# Resumen del árbol en el archivo de salida

arbol.resumen_a_txt(txt_path = ARBOL_OUTPUT)

# Mostrar el dibujo del árbol

plotter.add_axes()
plotter.show()
