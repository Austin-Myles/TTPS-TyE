from collections import defaultdict

def count_connected_components(nodes, edges):
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

# Procesamiento del input y ejecución del código
def process_input(input_lines):
    results = []
    t = int(input_lines[0].strip())  # Número de casos de prueba
    line_index = 1
    for _ in range(t):
        line_index += 1  # Saltar la línea en blanco
        largest_node = input_lines[line_index].strip()
        nodes = [chr(i) for i in range(ord('A'), ord(largest_node) + 1)]
        line_index += 1
        
        edges = []
        while line_index < len(input_lines) and input_lines[line_index].strip():
            edge = input_lines[line_index].strip()
            edges.append((edge[0], edge[1]))
            line_index += 1
        
        # Contar componentes
        components = count_connected_components(nodes, edges)
        results.append(str(components))
        
        line_index += 1  # Saltar la línea en blanco entre casos
    
    # Formatear la salida
    return "\n\n".join(results)

# Ejemplo de uso
input_data = """1

E
AB
CE
DB
EC
"""
input_lines = input_data.splitlines()
output = process_input(input_lines)
print(output)  # Debería imprimir el número de componentes para cada caso
