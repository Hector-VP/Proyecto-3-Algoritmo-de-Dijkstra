import random
import math
from clases_base import Grafo

def grafoGeografico(n, r, dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)

    # 1. Crea los "n" nodos asignándoles coordenadas aleatorias
    for i in range(n):
        id_nodo = str(i)
        # random.random() devuelve un valor de punto flotante en [0.0, 1.0)
        x_aleatorio = random.random()
        y_aleatorio = random.random()
        
        # Utiliza la función base que ya acepta "x" e "y"
        grafo.agregar_nodo(id_nodo, x_aleatorio, y_aleatorio)

    # 2. Compara todos los pares posibles de nodos
    for i in range(n):
        inicio_j = 0 if dirigido else i + 1
        
        for j in range(inicio_j, n):
            if i != j:
                # Recupera los objetos "nodo" del diccionario para acceder a sus coordenadas
                nodo_u = grafo.nodos[str(i)]
                nodo_v = grafo.nodos[str(j)]
                
                # 3. Calcula la distancia euclidiana
                distancia = math.sqrt((nodo_v.x - nodo_u.x)**2 + (nodo_v.y - nodo_u.y)**2)
                
                # 4. Si están dentro del radio "r", crea la conexión
                if distancia <= r:
                    grafo.agregar_arista(str(i), str(j))

    return grafo