from clases_base import Grafo
def DFS_R(grafo, s):
        """Búsqueda en Profundidad (Recursiva). Retorna el árbol inducido."""
        arbol = Grafo(grafo.dirigido)
        if s not in grafo.nodos:
            return arbol
            
        adyacencia = grafo._construir_adyacencia()
        visitados = set()
        
        def _dfs_recursivo(padre, actual):
            visitados.add(actual)
            
            nodo_obj = grafo.nodos[actual]
            arbol.agregar_nodo(actual, nodo_obj.x, nodo_obj.y)
            
            if padre is not None:
                arbol.agregar_arista(padre, actual)
                
            for vecino in adyacencia[actual]:
                if vecino not in visitados:
                    _dfs_recursivo(actual, vecino)
                    
        _dfs_recursivo(None, s)
        return arbol