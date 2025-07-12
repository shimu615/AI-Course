def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []                         # Initial path list
    if visited is None:
        visited = set()                  # Visited set banai
    path.append(start)                   # Current node add kori path-e
    visited.add(start)                   # Mark node as visited
    if start == goal:
        print("Path to goal:", path)     # Goal pele print
        return
    for neighbor in graph.get(start, []):    # Neighbor gulo check kori
        if neighbor not in visited:
            dfs(graph, neighbor, goal, path.copy(), visited.copy())

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A', 'F')
