import random
from clases_base import Grafo

def grafoErdosRenyi(n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)

    # 1. Crea los "n" nodos de manera aislada
    for i in range(n):
        # Utiliza el índice como ID del nodo (ej. "0", "1", "2"...)
        grafo.agregar_nodo(str(i))

    # 2. Calcula el máximo teórico de aristas para evitar un bucle infinito 
    #    si se pide un "m" mayor al que el grafo puede soportar.
    max_aristas = n * (n - 1) if dirigido else n * (n - 1) // 2
    if m > max_aristas:
        print(f"Advertencia: Se solicitarón {m} aristas y el máximo es {max_aristas}. Ajustando 'm'.")
        m = max_aristas

    # 3. Genera las aristas aleatoriamente
    aristas_creadas = 0
    
    while aristas_creadas < m:
        # Selecciona dos identificadores de nodo al azar
        u = str(random.randint(0, n - 1))
        v = str(random.randint(0, n - 1))

        # En los grafos simples no se permiten bucles (aristas de un nodo a sí mismo)
        if u != v:
            # Determina cómo sería el ID de esta posible arista
            if dirigido:
                id_temp = f"{u}->{v}"
            else:
                id_temp = f"{min(u, v)}--{max(u, v)}"

            # Verifica en O(1) si la arista ya existe en nuestro diccionario
            if id_temp not in grafo.aristas:
                # Si no existe, la agrega y aumenta nuestro contador
                grafo.agregar_arista(u, v)
                aristas_creadas += 1

    return grafo