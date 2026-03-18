import random
from clases_base import Grafo

def grafoGilbert(n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)

    # 1. Crea los "n" nodos
    for i in range(n):
        grafo.agregar_nodo(str(i))

    # 2. Evalua cada par posible de nodos
    for i in range(n):
        # Optimización: Si el grafo NO es dirigido, no necesita evaluar el par (j, i) 
        # si ya evaluó (i, j). Por lo tanto, "j" puede empezar desde (i + 1).
        # Si es dirigido, debe evaluar todas las combinaciones, empezando "j" desde 0.
        inicio_j = 0 if dirigido else i + 1
        
        for j in range(inicio_j, n):
            # Evita crear bucles (aristas de un nodo a sí mismo)
            if i != j:
                # random.random() genera un flotante uniforme en el intervalo [0.0, 1.0)
                probabilidad_actual = random.random()
                
                # Si el valor aleatorio entra en el umbral "p", crea la arista
                if probabilidad_actual <= p:
                    grafo.agregar_arista(str(i), str(j))

    return grafo