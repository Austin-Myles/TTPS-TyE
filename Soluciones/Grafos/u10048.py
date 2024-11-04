import sys
import heapq
from collections import defaultdict

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
    C, S, Q = map(int, sys.stdin.readline().strip().split())
    case = 1
    output = []

    while C != 0 and S != 0 and Q != 0:
        output.append("Case #"+ str(case))
        grafo = defaultdict(list)
        for _ in range(S):
            u, v, peso = map(int, sys.stdin.readline().strip().split())
            grafo[u].append((v, peso))
            grafo[v].append((u, peso))
        distancias = floyd(grafo, (C + 1))

        for _ in range(Q):
            start, end = map(int, sys.stdin.readline().strip().split())
            result = distancias[start][end]
            if result == float("inf"):
                output.append("no path")
            else:
                output.append(str(result))

        C, S, Q = map(int, sys.stdin.readline().strip().split())
        case += 1
        output.append("")

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
