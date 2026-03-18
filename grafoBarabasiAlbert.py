import random
from clases_base import Grafo

def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: número de aristas a añadir por cada nuevo nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)
    
    # Esta es nuestra "urna" para la selección proporcional
    nodos_prob = []

    # 1. Crear los primeros 'd' nodos y conecta todos contra todos
    for i in range(d):
        grafo.agregar_nodo(str(i))
        
    for i in range(d):
        for j in range(i + 1, d):
            grafo.agregar_arista(str(i), str(j))
            nodos_prob.append(str(i))
            nodos_prob.append(str(j))

    # 2. Agregar los nodos restantes uno por uno
    for i in range(d, n):
        nuevo_nodo = str(i)
        grafo.agregar_nodo(nuevo_nodo)

        # Usamos un conjunto para asegurar que conectamos a "d" nodos DISTINTOS
        objetivos = set()
        
        while len(objetivos) < d and len(nodos_prob) > 0:
            # Elige un nodo al azar de nuestra urna
            candidato = random.choice(nodos_prob)
            
            # Verifica que no sea el mismo nodo (evita bucles) 
            # y que no lo haya elegido anteriorment
            if candidato != nuevo_nodo and candidato not in objetivos:
                objetivos.add(candidato)

        # 3. Crea las aristas hacia los nodos elegidos y actualiza la urna
        for objetivo in objetivos:
            grafo.agregar_arista(nuevo_nodo, objetivo)
            nodos_prob.append(nuevo_nodo)
            nodos_prob.append(objetivo)

    return grafo