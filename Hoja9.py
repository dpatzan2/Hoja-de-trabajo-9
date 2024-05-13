import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo(archivo):
    G = nx.Graph()
    with open(archivo, 'r') as file:
        for line in file:
            origen, destino, costo = line.strip().split(',')
            G.add_edge(origen.strip(), destino.strip(), weight=int(costo))
    return G

def mostrar_destinos(grafo, origen):
    destinos = nx.single_source_dijkstra_path(grafo, origen)
    costos = nx.single_source_dijkstra_path_length(grafo, origen)
    print(f"Destinos posibles desde {origen}:")
    for destino, costo in costos.items():
        print(f"- {destino}: {costo}")

def encontrar_rutas(grafo, origen):
    rutas = nx.single_source_dijkstra_path(grafo, origen)
    costos = nx.single_source_dijkstra_path_length(grafo, origen)
    print(f"Rutas más baratas desde {origen}:")
    for destino, ruta in rutas.items():
        costo = costos[destino]
        print(f"- {destino}: {' -> '.join(ruta)} (Costo: {costo})")

# Crear el grafo a partir del archivo rutas.txt
grafo = crear_grafo('rutas.txt')

# Solicitar al usuario la estación de salida
estacion_salida = input("Ingrese la estación de salida: ")

# Mostrar los destinos posibles y sus costos
mostrar_destinos(grafo, estacion_salida)

# Encontrar las rutas más baratas a cada destino
encontrar_rutas(grafo, estacion_salida)

# Mostrar el grafo de destinos
nx.draw(grafo, with_labels=True)
plt.show()