def count_components(graph, nodes):
    visited = set()  # Para llevar un registro de los nodos visitados

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    component_count = 0
    for node in nodes:
        if node not in visited:
            visited.add(node)
            dfs(node)
            component_count += 1

    return component_count

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['E'],
    'E': ['D']
}
nodes = ['A', 'B', 'C', 'D', 'E']  # Lista de todos los nodos
print("Número de componentes conectados:", count_components(graph, nodes))
