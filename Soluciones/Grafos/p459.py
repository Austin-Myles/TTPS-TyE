from collections import defaultdict
import sys

def count_components(nodes, edges):
    # Construir el grafo
    grafo = defaultdict(list)
    for edge in edges:
        u, v = edge
        grafo[u].append(v)
        grafo[v].append(u)
    
    # DFS para encontrar componentes conexas
    visited = {node: False for node in nodes}

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for neighbor in grafo[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    # Contar componentes
    component_count = 0
    for node in nodes:
        if not visited[node]:
            dfs(node)
            component_count += 1

    return component_count

def main():
    output = []
    cases = int(sys.stdin.readline())
    sys.stdin.readline() # For the blank line.
    for _ in range(cases):
        ln = sys.stdin.readline().strip() # Largest node in the graph.
        nodos = [chr(i) for i in range(ord('A'), ord(ln) + 1)]
        aristas = []
        while(True):
            aux = sys.stdin.readline().strip()
            if aux:
                aristas.append(aux)
            else:
                break
        component_count = count_components(nodos, aristas)
        output.append(str(component_count))

    sys.stdout.write("\n\n".join(output) + "\n")
    
if __name__ == "__main__":
    main()
