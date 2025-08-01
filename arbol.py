ARBOL_H = "habilidades_ninja.txt"
class NodoHabilidad:
    def _init_(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
def crear_arbol_habilidades(fuerza, agilidad, resistencia):
    raiz = NodoHabilidad(fuerza)
    raiz.izquierda = NodoHabilidad(agilidad)
    raiz.derecha = NodoHabilidad(resistencia)
    return raiz
def guardar_arbol(nombre, arbol):
    with open(ARBOL_H, "a", encoding="utf-8") as f:
        f.write(f"{nombre}: {arbol.valor}, {arbol.izquierda.valor},{arbol.derecha.valor}\n")
