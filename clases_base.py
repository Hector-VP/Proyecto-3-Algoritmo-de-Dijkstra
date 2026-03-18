class Nodo:
    def __init__(self, id_nodo, x=0.0, y=0.0):
        """
        Esta clase representa un vértice en el grafo.
        """
        self.id = id_nodo
        self.x = x  # Coordenada X, útil para el modelo geográfico
        self.y = y  # Coordenada Y, útil para el modelo geográfico
        self.grado = 0 # Mantener un registro del grado optimizará Barabási-Albert

    def __str__(self):
        return f"Nodo({self.id})"


class Arista:
    def __init__(self, origen, destino, dirigido=False):
        """
        Esta clase representa un enlace entre dos nodos.
        """
        self.origen = origen
        self.destino = destino
        self.dirigido = dirigido
        
        # Generamos un ID único para la arista para evitar duplicados en el grafo
        if dirigido:
            self.id = f"{origen.id}->{destino.id}"
        else:
            # Si no es dirigido, ordenamos los ID's para que A--B sea idéntico que B--A
            self.id = f"{min(origen.id, destino.id)}--{max(origen.id, destino.id)}"

    def __str__(self):
        return self.id


class Grafo:
    def __init__(self, dirigido=False):
        """
        Esta clase gestiona la colección de nodos y aristas.
        """
        self.dirigido = dirigido
        self.nodos = {}   # Diccionario para acceso en O(1)
        self.aristas = {} # Diccionario para evitar multígrafos en O(1)

    def agregar_nodo(self, id_nodo, x=0.0, y=0.0):
        """Añade un nodo al grafo si este no existe previamente."""
        if id_nodo not in self.nodos:
            self.nodos[id_nodo] = Nodo(id_nodo, x, y)

    def agregar_arista(self, id_origen, id_destino):
        """Añade una arista conectando dos nodos. Además crea los nodos si no existen."""
        # Valida la existencia de los nodos y los crea si no existen
        if id_origen not in self.nodos:
            self.agregar_nodo(id_origen)
        if id_destino not in self.nodos:
            self.agregar_nodo(id_destino)

        nodo_origen = self.nodos[id_origen]
        nodo_destino = self.nodos[id_destino]

        # Evita bucles (aristas de un nodo a sí mismo) si la lógica lo requiere.
        if id_origen == id_destino:
            return

        nueva_arista = Arista(nodo_origen, nodo_destino, self.dirigido)

        # Inserta la arista solo si no existe ya
        if nueva_arista.id not in self.aristas:
            self.aristas[nueva_arista.id] = nueva_arista
            
            # Actualiza los grados de los nodos en tiempo constante O(1)
            nodo_origen.grado += 1
            if not self.dirigido:
                nodo_destino.grado += 1

    def guardar_graphviz(self, nombre_archivo):
        """Exporta el grafo a un archivo con formato simple de GraphViz (.gv)"""
        tipo_grafo = "digraph" if self.dirigido else "graph"
        conector = "->" if self.dirigido else "--"

        with open(nombre_archivo, 'w') as f:
            f.write(f"{tipo_grafo} G {{\n")
            for arista in self.aristas.values():
                f.write(f"    {arista.origen.id} {conector} {arista.destino.id};\n")
            f.write("}\n")