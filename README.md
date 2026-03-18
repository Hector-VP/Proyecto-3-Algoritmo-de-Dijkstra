# Generador de Grafos y Modelos de Redes Complejas

**Institución:** Centro de Investigación en Computación (CIC - IPN)  
**Profesor:** Dr. Rolando Quintero Téllez  
**Autor:** Héctor David Valdés Pastrana  

---

## Descripción del Proyecto

Esta biblioteca, desarrollada en Python 3 bajo el paradigma de Programación Orientada a Objetos (POO), proporciona las estructuras de datos fundamentales para la creación, manipulación y exportación de grafos. 

El proyecto incluye la implementación de las clases base `Nodo`, `Arista` y `Grafo`, así como algoritmos para la generación de redes estocásticas y deterministas utilizando seis de los modelos más importantes en la teoría de redes complejas.

## Modelos de Generación Implementados

1. **Modelo $G_{m,n}$ de Malla:** Generación de redes reticulares bidimensionales.
2. **Modelo $G_{n,m}$ de Erdös y Rényi:** Generación de redes aleatorias con un número fijo de aristas.
3. **Modelo $G_{n,p}$ de Gilbert:** Generación de redes aleatorias basándose en una probabilidad $p$ de conexión.
4. **Modelo $G_{n,r}$ Geográfico Simple:** Generación espacial basada en distancia euclidiana.
5. **Variante del modelo $G_{n,d}$ de Barabási-Albert:** Crecimiento de red basado en conexión preferencial (redes libres de escala).
6. **Modelo $G_n$ de Dorogovtsev-Mendes:** Crecimiento de red favoreciendo un alto coeficiente de agrupamiento.

## Arquitectura del Proyecto

El código está estructurado de forma modular para facilitar su escalabilidad y mantenimiento:

* `clases_base.py`: Núcleo de estructuras de datos (Clases Nodo, Arista y Grafo).
* `main.py`: Script principal de ejecución y orquestación.
* Archivos individuales por modelo (`malla.py`, `erdos.py`, `gilbert.py`, etc...).
* `grafos_gv/`: Directorio con los 18 archivos generados en formato GraphViz (`.gv`) para 50, 200 y 500 nodos.
* `imagenes/`: Directorio con las representaciones visuales renderizadas.

## Requisitos y Uso

El código está escrito en Python estándar y no requiere dependencias externas para la generación de la topología.

Para generar los archivos `.gv` automáticamente, ejecuta:

```bash
python3 main.py