from clases_base import Grafo

def DFS_I(grafo, s):
    """Búsqueda en Profundidad (Iterativa). Retorna el árbol inducido."""
    arbol = Grafo(grafo.dirigido)
    
    if s not in grafo.nodos:
        return arbol
        
    adyacencia = grafo._construir_adyacencia()
    visitados = set()
    pila = [(None, s)]
    
    while pila:
        padre, actual = pila.pop()
        
        if actual not in visitados:
            visitados.add(actual)
            
            nodo_obj = grafo.nodos[actual]
            arbol.agregar_nodo(actual, nodo_obj.x, nodo_obj.y)
            
            if padre is not None:
                arbol.agregar_arista(padre, actual)
            
            # reversed() asegura que el orden de exploración por la derecha sea el estándar
            for vecino in reversed(adyacencia[actual]):
                if vecino not in visitados:
                    pila.append((actual, vecino))
                    
    return arbol