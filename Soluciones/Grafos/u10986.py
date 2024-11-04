from collections import defaultdict
import sys

# RUNTIME ERROR - u10048

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight
        
def dijkstra(grafo, inicio, destino):
    L = {(inicio, nodo): float("inf") for nodo in grafo}
    L[(inicio, inicio)] = 0
    S = set()
    prev = {nodo: None for nodo in grafo}
    while len(S) < len(grafo):
        u = min (((inicio, nodo) for nodo in grafo if (inicio, nodo) not in S),  key=lambda nodo: L[nodo])
        S.add(u)
        for v, peso in grafo[u[1]].items():
            if (inicio, v) not in S:
                if peso == "inf":
                    peso = float("inf")
                if L[u] + peso < L[(inicio, v)]:
                    L[(inicio, v)] = L[u] + peso
                    prev[v] = u[1]
    nodo_act = destino
    camino = []
    while nodo_act is not None:
        camino.append(nodo_act)
        nodo_act = prev[nodo_act]

    return L, camino

def main():
    #output = [] # Para luego imprimir el output
    N = sys.stdin.readline().strip() # Número de casos de prueba
    for i in range(int(N)):
        G = Graph()
        aux = sys.stdin.readline().strip().split(" ")
        n, m, S, T = int(aux[0]), int(aux[1]), int(aux[2]), int(aux[3])
        if m == 0:
            sys.stdout.write("Case #" + str(i+1) + ": unreachable\n")
            continue
        for _ in range(m):
            gaux = sys.stdin.readline().strip().split(" ")
            u, v, weight = int(gaux[0]), int(gaux[1]), int(gaux[2])
            G.add_edge(u, v, weight)
        #print(G.graph)
        if S > T:
            distancias, camino = dijkstra(G.graph, T, S)
            distancia_total = distancias[(T, S)]
        else:
            distancias, camino = dijkstra(G.graph, S, T)
            distancia_total = distancias[(S, T)]

        sys.stdout.write("Case #" + str(i+1) + ": " + str(distancia_total) + "\n")
    #sys.stdout.write("\n".join(output).strip() + "\n")
    
if __name__ == "__main__":
    main()
