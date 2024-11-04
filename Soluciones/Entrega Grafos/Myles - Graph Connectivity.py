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
    output = [] # Generamos un vector output para ir concatenando las respuestas.
    cases = int(sys.stdin.readline()) # Obtenemos los casos
    sys.stdin.readline() # Nos saltamos la linea en blanco.
    for _ in range(cases):
        ln = sys.stdin.readline().strip() # Obtenemos la letra mas grande del grafo y a partir de ella creamos el grafo. 
        nodos = [chr(i) for i in range(ord('A'), ord(ln) + 1)] # Definimos los nodos de manera ordinal.
        aristas = [] # Definimos un vector para las aristas.
        while(True):
            aux = sys.stdin.readline().strip() # Obtenemos las aristas hasta llegar a un caracter en blanco.
            if aux:
                aristas.append(aux)
            else:
                break
        component_count = count_components(nodos, aristas) # Obtenemos la cantidad de componentes conexas.
        output.append(str(component_count))

    sys.stdout.write("\n\n".join(output) + "\n")
    
if __name__ == "__main__":
    main()
