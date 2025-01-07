import json

from constantes import *
from models.generadorJSONRama import GeneradorJSONRama

class GeneradorJSONArbol:

    def __init__(self, max_niveles: int = MAX_NIVELES) -> None:
        self.arbol: dict = self.generar_arbol(max_niveles = max_niveles)
    
    def generar_arbol(self, max_niveles: int = MAX_NIVELES) -> dict:
        generadorJSONRama = GeneradorJSONRama(nivel = 0, max_niveles = MAX_NIVELES)
        arbol_dict = generadorJSONRama.generar_rama(nivel = 0, max_niveles = max_niveles, longitud_rama_madre = 0, grosor_rama_madre = 0)
        return arbol_dict
    
