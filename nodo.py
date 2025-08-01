def recorrido_por_estrategia(arbol, status, lista):
    if status == "ganando":
        preorden(arbol, lista)
    elif status == "empatado":
        inorden(arbol, lista)
    else:
        postorden(arbol,lista)

def preorden(nodo, lista):
    if nodo:
        lista.append(nodo.valor)
        preorden(nodo.izquierda, lista)
        preorden(nodo.derecha, lista)

def inorden(nodo, lista):
    if nodo:
        inorden(nodo.izquierda, lista)
        lista.append(nodo.valor)
        inorden(nodo.derecha, lista)

def postorden(nodo, lista):
    if nodo:
        postorden(nodo.izquierda, lista)
        postorden(nodo.derecha, lista)
        lista.append(nodo.valor)
