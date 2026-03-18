import os
# Importas cada función desde su archivo específico
from grafoMalla import grafoMalla
from grafoErdosRenyi import grafoErdosRenyi
from grafoGilbert import grafoGilbert
from grafoGeografico import grafoGeografico
from grafoBarabasiAlbert import grafoBarabasiAlbert
from grafoDorogovtsevMendes import grafoDorogovtsevMendes

def generar_archivos_proyecto():
    """
    Función principal para automatizar la generación de los 18 grafos
    requeridos en el proyecto.
    """
    # Crea un directorio para mantener los archivos ordenados
    carpeta_salida = "grafos_gv"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Los tres tamaños solicitados en la rúbrica
    tamanos = [50, 200, 500]

    print("Iniciando la generación automática de grafos...\n")

    for n in tamanos:
        print(f"--- Generando modelos para {n} nodos ---")
        
        # 1. Modelo de Malla 
        # Ajusta "m" y "n" filas para que su multiplicación sea exactamente "n"
        if n == 50: m, filas = 5, 10
        elif n == 200: m, filas = 10, 20
        elif n == 500: m, filas = 20, 25
        
        grafo_malla = grafoMalla(m, filas, dirigido=False)
        grafo_malla.guardar_graphviz(f"{carpeta_salida}/malla_{n}.gv")
        print(f"✔ Malla {n} (m={m}, filas={filas}) generado.")

        # 2. Modelo Erdös-Rényi 
        # Elege un número de aristas "m" proporcional al doble de nodos
        m_aristas = n * 2
        grafo_erdos = grafoErdosRenyi(n, m_aristas, dirigido=False)
        grafo_erdos.guardar_graphviz(f"{carpeta_salida}/erdos_{n}.gv")
        print(f"✔ Erdös-Rényi {n} (m={m_aristas} aristas) generado.")

        # 3. Modelo Gilbert 
        # Una probabilidad del 10% resulta en grafos conexos pero no saturados
        p = 0.1
        grafo_gilbert = grafoGilbert(n, p, dirigido=False)
        grafo_gilbert.guardar_graphviz(f"{carpeta_salida}/gilbert_{n}.gv")
        print(f"✔ Gilbert {n} (p={p}) generado.")

        # 4. Modelo Geográfico Simple
        # Un radio de 0.2 en un espacio unitario da una buenas agrupación espacial
        r = 0.2
        grafo_geo = grafoGeografico(n, r, dirigido=False)
        grafo_geo.guardar_graphviz(f"{carpeta_salida}/geografico_{n}.gv")
        print(f"✔ Geográfico {n} (r={r}) generado.")

        # 5. Modelo Barabási-Albert
        # Un grado "d=4" genera 'hubs' muy distinguibles en la visualización
        d = 4
        grafo_barabasi = grafoBarabasiAlbert(n, d, dirigido=False)
        grafo_barabasi.guardar_graphviz(f"{carpeta_salida}/barabasi_{n}.gv")
        print(f"✔ Barabási-Albert {n} (d={d}) generado.")

        # 6. Modelo Dorogovtsev-Mendes
        grafo_dorogovtsev = grafoDorogovtsevMendes(n, dirigido=False)
        grafo_dorogovtsev.guardar_graphviz(f"{carpeta_salida}/dorogovtsev_{n}.gv")
        print(f"✔ Dorogovtsev-Mendes {n} generado.\n")

    print(f" Los 18 archivos .gv se han guardado en la carpeta '{carpeta_salida}'.")

# Punto de entrada estándar en Python
if __name__ == "__main__":
    generar_archivos_proyecto()