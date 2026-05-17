from clases_base import Grafo
from collections import deque

def BFS(grafo, s):
    """Búsqueda en lo Ancho. Retorna el árbol inducido como un nuevo objeto Grafo."""
    # Cambiamos self por grafo en todo el bloque
    arbol = Grafo(grafo.dirigido)
    
    if s not in grafo.nodos:
        return arbol
        
    adyacencia = grafo._construir_adyacencia()
    visitados = {s}
    cola = deque([(None, s)])
    
    while cola:
        padre, actual = cola.popleft()
        
        # Agrega el nodo conservando sus coordenadas si existen
        nodo_obj = grafo.nodos[actual]
        arbol.agregar_nodo(actual, nodo_obj.x, nodo_obj.y)
        
        if padre is not None:
            arbol.agregar_arista(padre, actual)
            
        for vecino in adyacencia[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((actual, vecino))
                
    return arbol