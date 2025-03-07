def connected(nodes, edges):
    if not nodes:
        return True
    graph = {node: set() for node in nodes}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    dfs(nodes[0])
    return len(visited) == len(nodes)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges))  # True
