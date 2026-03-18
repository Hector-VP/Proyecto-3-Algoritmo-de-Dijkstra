import random
from clases_base import Grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
    :param n: número de nodos (>= 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)

    # El modelo requiere estrictamente empezar con un triángulo
    if n < 3:
        print("Error: El modelo Dorogovtsev-Mendes requiere al menos 3 nodos.")
        return grafo

    # 1. Crea el triángulo inicial (3 nodos, 3 aristas)
    for i in range(3):
        grafo.agregar_nodo(str(i))

    grafo.agregar_arista("0", "1")
    grafo.agregar_arista("1", "2")
    grafo.agregar_arista("2", "0")

    # Lista auxiliar para elegir aristas al azar de forma eficiente
    # Guarda tuplas con los ID's de los nodos origen y destino
    aristas_disponibles = [("0", "1"), ("1", "2"), ("2", "0")]

    # 2. Agrega los nodos restantes (desde el índice 3 hasta n-1)
    for i in range(3, n):
        nuevo_nodo = str(i)
        grafo.agregar_nodo(nuevo_nodo)

        # Selecciona una arista existente uniformemente al azar
        arista_elegida = random.choice(aristas_disponibles)
        nodo_u = arista_elegida[0]
        nodo_v = arista_elegida[1]

        # Conecta el nuevo nodo a los extremos de la arista elegida
        grafo.agregar_arista(nuevo_nodo, nodo_u)
        grafo.agregar_arista(nuevo_nodo, nodo_v)

        # Añade las dos nuevas aristas a nuestra lista de selección
        # para que los futuros nodos puedan elegirlas
        aristas_disponibles.append((nuevo_nodo, nodo_u))
        aristas_disponibles.append((nuevo_nodo, nodo_v))

    return grafo