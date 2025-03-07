def find_components(nodes, edges):
    graph = {node: set() for node in nodes}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    visited = set()
    components = []
    def dfs(node, comp):
        visited.add(node)
        comp.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)
    for node in nodes:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(sorted(comp))
    return sorted(components, key=lambda comp: comp[0])

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges))  # [[1, 2, 3, 4, 5]]
