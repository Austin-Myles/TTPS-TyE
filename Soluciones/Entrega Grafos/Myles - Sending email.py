import sys
import heapq
from collections import defaultdict

def dijkstra(grafo, start, n):
    # Distancias inicializadas en infinito y la distancia del mismo elemento sera 0
    distancias = [float("inf")] * n
    distancias[start] = 0
    
    # Cola de prioridad para Dijkstra
    pq = [(0, start)]
    while pq:
        curr_dist, nodo = heapq.heappop(pq)
        
        # Si la distancia es mayor que la almacenada, la ignoramos
        if curr_dist > distancias[nodo]:
            continue
        
        # Relajamos los vecinos
        for vec, peso in grafo[nodo]:
            distancia = curr_dist + peso
            
            if distancia < distancias[vec]:
                distancias[vec] = distancia
                heapq.heappush(pq, (distancia, vec))
    
    return distancias

def main():
    input = sys.stdin.read # Obtenemos todo el input
    data = input().strip().splitlines()
    
    t = int(data[0])  # Número de casos
    idx = 1 # Índice de lectura ya que leemos todo el input.
    output = [] # Generamos un vector output para ir concatenando las respuestas.
    for case in range(1, t + 1):
        n, m, start, end = map(int, data[idx].split()) # Leemos los datos de cada caso
        idx += 1
        
        grafo = defaultdict(list)
        for _ in range(m):
            u, v, peso = map(int, data[idx].split()) # Obtenemos cada arista junto con su peso
            grafo[u].append((v, peso))
            grafo[v].append((u, peso))
            idx += 1
        
        distancias = dijkstra(grafo, start, n) # Calculamos todas las distancias del elemento start
         
        result = distancias[end] # Obtenemos la distancia del elemento end
        if result == float("inf"):
            output.append(f"Case #{case}: unreachable")
        else:
            output.append(f"Case #{case}: {result}")
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()
