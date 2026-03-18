from clases_base import Grafo

def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    # 1. Instancia nuestro objeto Grafo
    grafo = Grafo(dirigido)

    # 2. Recorre las columnas "m" y las filas "n"
    for i in range(m):
        for j in range(n):
            # Crea un identificador visualmente claro para el nodo actual
            id_actual = f"n_{i}_{j}"
            
            # Aquí asegura que el nodo exista en el grafo. 
            # (Aunque agregar arista lo hace automáticamente, esto garantiza 
            # que los nodos sin conexiones también se creen de ser el caso).
            grafo.agregar_nodo(id_actual)

            # 3. Conexión horizontal: Vecino de la derecha (i+1, j)
            # Solo conecta si no ha llegado al borde derecho (i < m - 1)
            if i + 1 < m:
                id_derecha = f"n_{i+1}_{j}"
                grafo.agregar_arista(id_actual, id_derecha)

            # 4. Conexión vertical: Vecino de abajo (i, j+1)
            # Solo conecta si no ha llegado al borde inferior (j < n - 1)
            if j + 1 < n:
                id_abajo = f"n_{i}_{j+1}"
                grafo.agregar_arista(id_actual, id_abajo)

    return grafo