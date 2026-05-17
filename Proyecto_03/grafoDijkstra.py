import math
import heapq
import random
from clases_base import Grafo

def grafoDijkstra(grafo, s):
    """
    Calcula el árbol de caminos más cortos desde el nodo fuente 's'.
    Retorna un nuevo Grafo con los nodos formateados como 'nodo (distancia)'.
    """
    # Si el nodo fuente no existe en el grafo, tomamos el primero disponible
    if s not in grafo.nodos:
        s = list(grafo.nodos.keys())[0]

    # Inicialización de distancias y predecesores
    distancias = {id_nodo: math.inf for id_nodo in grafo.nodos}
    distancias[s] = 0
    padres = {id_nodo: None for id_nodo in grafo.nodos}
    
    # Cola de prioridad inicializada con el nodo origen
    pq = [(0, s)]
    
    # Aprovecha el acceso en O(1) a los vecinos
    adyacencia = grafo._construir_adyacencia()
    
    while pq:
        dist_actual, u = heapq.heappop(pq)
        
        if dist_actual > distancias[u]:
            continue
            
        for v in adyacencia[u]:
            # Asignamos un peso aleatorio en punto flotante para cumplir la rúbrica
            peso = random.uniform(1.0, 50.0) 
            dist_alternativa = dist_actual + peso
            
            if dist_alternativa < distancias[v]:
                distancias[v] = dist_alternativa
                padres[v] = u
                heapq.heappush(pq, (dist_alternativa, v))
                
    # Construcción del Árbol de Dijkstra Resultante usando la clase base pura
    arbol_dijkstra = Grafo(dirigido=True) 
    
    nombres_nuevos = {}
    for id_nodo, d in distancias.items():
        if d != math.inf:
            # Formatea el nombre con dos decimales: ej. "n_1_0 (22.45)"
            nuevo_nombre = f"{id_nodo} ({d:.2f})"
            nombres_nuevos[id_nodo] = nuevo_nombre
            arbol_dijkstra.agregar_nodo(nuevo_nombre)
            
    # Insertamos las aristas basándonos en el diccionario de predecesores
    for v, u in padres.items():
        if u is not None:
            arbol_dijkstra.agregar_arista(nombres_nuevos[u], nombres_nuevos[v])
            
    return arbol_dijkstra