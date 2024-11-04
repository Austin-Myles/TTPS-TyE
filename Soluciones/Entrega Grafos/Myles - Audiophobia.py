import sys
import heapq
from collections import defaultdict

#En esta solución se hizo uso del algoritmo de Floyd para encontrar el camino más corto entre dos nodos

def floyd(grafo, n):
    # Inicializamos las distancias
    distancias = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        distancias[u][u] = 0

    # Cargamos las distancias conocidas
    for u in grafo:
        for v, peso in grafo[u]:
            distancias[u][v] = peso
            distancias[v][u] = peso
    
    # Calculamos las distancias
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distancias[i][j] = min(distancias[i][j], max(distancias[i][k], distancias[k][j]))
    
    return distancias

def main():
    C, S, Q = map(int, sys.stdin.readline().strip().split()) # Cantidad de ciudades, calles y consultas
    case = 1
    output = [] # Generamos un vector output para ir concatenando las respuestas.

    while C != 0 and S != 0 and Q != 0: # Condición de corte del enunciado
        output.append("Case #"+ str(case)) # Agregamos el caso actual al output
        grafo = defaultdict(list)
        for _ in range(S): # Cargamos todas las aristas proporcionadas por el input a la estructura de grafo.
            u, v, peso = map(int, sys.stdin.readline().strip().split())
            grafo[u].append((v, peso))
            grafo[v].append((u, peso))

        distancias = floyd(grafo, (C + 1)) # Calculamos las distancias entre todos los nodos

        for _ in range(Q):
            start, end = map(int, sys.stdin.readline().strip().split())
            result = distancias[start][end] # Obtenemos la distancia entre los nodos start y end
            if result == float("inf"): # Si no hay camino, agregamos "no path" al output
                output.append("no path")
            else:
                output.append(str(result))

        C, S, Q = map(int, sys.stdin.readline().strip().split()) # Leemos nuevamente para seguir con el siguente caso.
        case += 1
        output.append("")

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
