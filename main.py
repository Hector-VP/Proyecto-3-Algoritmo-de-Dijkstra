import os
import sys

# Importa cada función desde su archivo específico
from grafoMalla import grafoMalla
from grafoErdosRenyi import grafoErdosRenyi
from grafoGilbert import grafoGilbert
from grafoGeografico import grafoGeografico
from grafoBarabasiAlbert import grafoBarabasiAlbert
from grafoDorogovtsevMendes import grafoDorogovtsevMendes

# Algoritmos del Proyecto 02 - Rutas actualizadas
from Proyecto_02 import grafoBFS
from Proyecto_02 import grafoDFS_I
from Proyecto_02 import grafoDFS_R

# Algoritmos del Proyecto 03 - Rutas actualizadas
from Proyecto_03.grafoDijkstra import grafoDijkstra

# Aumentamos el límite de recursividad por seguridad
sys.setrecursionlimit(2500)

def generar_archivos_proyecto3():
    """
    Función principal para generar los grafos base
    y sus árboles de caminos más cortos usando Dijkstra.
    """
    # Nueva carpeta para el Proyecto 3
    carpeta_salida = "grafos_dijkstra"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Requisito estricto: "pocos" y "muchos" nodos
    tamanos = [30, 500]
    nodo_fuente = 0

    print("Iniciando cálculo de caminos más cortos (Dijkstra)...\n")

    for n in tamanos:
        print(f"--- Procesando Modelos para {n} nodos ---")
        
        # 1. Modelo de Malla 
        if n == 30: m, filas = 5, 6
        elif n == 500: m, filas = 20, 25
        
        grafo_malla = grafoMalla(m, filas, dirigido=False)
        grafo_malla.guardar_graphviz(f"{carpeta_salida}/malla_{n}_original.gv")
        arbol_malla = grafoDijkstra(grafo_malla, nodo_fuente)
        arbol_malla.guardar_graphviz(f"{carpeta_salida}/malla_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Malla {n} y su árbol Dijkstra generados.")

        # 2. Modelo Erdös-Rényi 
        m_aristas = n * 2
        grafo_erdos = grafoErdosRenyi(n, m_aristas, dirigido=False)
        grafo_erdos.guardar_graphviz(f"{carpeta_salida}/erdos_{n}_original.gv")
        arbol_erdos = grafoDijkstra(grafo_erdos, nodo_fuente)
        arbol_erdos.guardar_graphviz(f"{carpeta_salida}/erdos_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Erdös-Rényi {n} y su árbol Dijkstra generados.")

        # 3. Modelo Gilbert 
        p = 0.1
        grafo_gilbert = grafoGilbert(n, p, dirigido=False)
        grafo_gilbert.guardar_graphviz(f"{carpeta_salida}/gilbert_{n}_original.gv")
        arbol_gilbert = grafoDijkstra(grafo_gilbert, nodo_fuente)
        arbol_gilbert.guardar_graphviz(f"{carpeta_salida}/gilbert_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Gilbert {n} y su árbol Dijkstra generados.")

        # 4. Modelo Geográfico Simple
        r = 0.2
        grafo_geo = grafoGeografico(n, r, dirigido=False)
        grafo_geo.guardar_graphviz(f"{carpeta_salida}/geografico_{n}_original.gv")
        arbol_geo = grafoDijkstra(grafo_geo, nodo_fuente)
        arbol_geo.guardar_graphviz(f"{carpeta_salida}/geografico_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Geográfico {n} y su árbol Dijkstra generados.")

        # 5. Modelo Barabási-Albert
        d = 4
        grafo_barabasi = grafoBarabasiAlbert(n, d, dirigido=False)
        grafo_barabasi.guardar_graphviz(f"{carpeta_salida}/barabasi_{n}_original.gv")
        arbol_barabasi = grafoDijkstra(grafo_barabasi, nodo_fuente)
        arbol_barabasi.guardar_graphviz(f"{carpeta_salida}/barabasi_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Barabási-Albert {n} y su árbol Dijkstra generados.")

        # 6. Modelo Dorogovtsev-Mendes
        grafo_dorogovtsev = grafoDorogovtsevMendes(n, dirigido=False)
        grafo_dorogovtsev.guardar_graphviz(f"{carpeta_salida}/dorogovtsev_{n}_original.gv")
        arbol_doro = grafoDijkstra(grafo_dorogovtsev, nodo_fuente)
        arbol_doro.guardar_graphviz(f"{carpeta_salida}/dorogovtsev_{n}_dijkstra.gv", color_arista="orange")
        print(f"✔ Dorogovtsev-Mendes {n} y su árbol Dijkstra generados.\n")

    print(f" Los archivos .gv se han guardado exitosamente en la carpeta '{carpeta_salida}'.")

if __name__ == "__main__":
    generar_archivos_proyecto3()