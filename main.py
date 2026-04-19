import os
import sys

# Importa cada función desde su archivo específico
from grafoMalla import grafoMalla
from grafoErdosRenyi import grafoErdosRenyi
from grafoGilbert import grafoGilbert
from grafoGeografico import grafoGeografico
from grafoBarabasiAlbert import grafoBarabasiAlbert
from grafoDorogovtsevMendes import grafoDorogovtsevMendes
from grafoBFS import BFS
from grafoDFS_I import DFS_I
from grafoDFS_R import DFS_R

# Aumentamos el límite de recursividad para que DFS_R soporte los grafos de 500 nodos
sys.setrecursionlimit(2500)

def guardar_arboles(grafo, nombre_modelo, n, s=0):
    """
    Toma el grafo generado, calcula sus 3 árboles desde el nodo 's'
    y los exporta con colores para contrastar en Gephi.
    """
    # Validación CRUCIAL: Si el nodo 's' (ej. 0) no existe, tomamos el primero disponible
    if s not in grafo.nodos:
        s = list(grafo.nodos.keys())[0]
    # BFS (Rojo)
    arbol_bfs = BFS(grafo,s)
    arbol_bfs.guardar_graphviz(f"grafos_gv/{nombre_modelo}_{n}_BFS.gv", color_arista="red")
    
    # DFS Iterativo (Azul)
    arbol_dfs_i = DFS_I(grafo,s)
    arbol_dfs_i.guardar_graphviz(f"grafos_gv/{nombre_modelo}_{n}_DFS_I.gv", color_arista="blue")
    
    # DFS Recursivo (Verde)
    arbol_dfs_r = DFS_R(grafo, s)
    arbol_dfs_r.guardar_graphviz(f"grafos_gv/{nombre_modelo}_{n}_DFS_R.gv", color_arista="green")

def generar_archivos_proyecto():
    """
    Función principal para automatizar la generación de los grafos base
    y sus respectivos árboles inducidos.
    """
    # Crea un directorio para mantener los archivos ordenados
    carpeta_salida = "grafos_gv"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Los tres TAMAÑOS NUEVOS solicitados en la rúbrica del Proyecto 2
    tamanos = [30, 100, 500]
    nodo_fuente = 0

    print("Iniciando la generación automática de grafos y árboles...\n")

    for n in tamanos:
        print(f"--- Generando modelos y árboles para {n} nodos ---")
        
        # Ajusta "m" y  "filas" para los nuevos tamaños (30, 100, 500)
        # 1. Modelo de Malla 
        if n == 30: m, filas = 5, 6
        elif n == 100: m, filas = 10, 10
        elif n == 500: m, filas = 20, 25
        
        grafo_malla = grafoMalla(m, filas, dirigido=False)
        grafo_malla.guardar_graphviz(f"{carpeta_salida}/malla_{n}.gv")
        guardar_arboles(grafo_malla, "malla", n, nodo_fuente)
        print(f"✔ Malla {n} (m={m}, filas={filas}) y sus 3 árboles generados.")

        # 2. Modelo Erdös-Rényi 
        m_aristas = n * 2
        grafo_erdos = grafoErdosRenyi(n, m_aristas, dirigido=False)
        grafo_erdos.guardar_graphviz(f"{carpeta_salida}/erdos_{n}.gv")
        guardar_arboles(grafo_erdos, "erdos", n, nodo_fuente)
        print(f"✔ Erdös-Rényi {n} (m={m_aristas} aristas) y sus 3 árboles generados.")

        # 3. Modelo Gilbert 
        p = 0.1
        grafo_gilbert = grafoGilbert(n, p, dirigido=False)
        grafo_gilbert.guardar_graphviz(f"{carpeta_salida}/gilbert_{n}.gv")
        guardar_arboles(grafo_gilbert, "gilbert", n, nodo_fuente)
        print(f"✔ Gilbert {n} (p={p}) y sus 3 árboles generados.")

        # 4. Modelo Geográfico Simple
        r = 0.2
        grafo_geo = grafoGeografico(n, r, dirigido=False)
        grafo_geo.guardar_graphviz(f"{carpeta_salida}/geografico_{n}.gv")
        guardar_arboles(grafo_geo, "geografico", n, nodo_fuente)
        print(f"✔ Geográfico {n} (r={r}) y sus 3 árboles generados.")

        # 5. Modelo Barabási-Albert
        d = 4
        grafo_barabasi = grafoBarabasiAlbert(n, d, dirigido=False)
        grafo_barabasi.guardar_graphviz(f"{carpeta_salida}/barabasi_{n}.gv")
        guardar_arboles(grafo_barabasi, "barabasi", n, nodo_fuente)
        print(f"✔ Barabási-Albert {n} (d={d}) y sus 3 árboles generados.")

        # 6. Modelo Dorogovtsev-Mendes
        grafo_dorogovtsev = grafoDorogovtsevMendes(n, dirigido=False)
        grafo_dorogovtsev.guardar_graphviz(f"{carpeta_salida}/dorogovtsev_{n}.gv")
        guardar_arboles(grafo_dorogovtsev, "dorogovtsev", n, nodo_fuente)
        print(f"✔ Dorogovtsev-Mendes {n} y sus 3 árboles generados.\n")

    print(f" Los 72 archivos .gv se han guardado en la carpeta '{carpeta_salida}'.")

# Punto de entrada estándar en Python
if __name__ == "__main__":
    generar_archivos_proyecto()