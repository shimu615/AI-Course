def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = []
    path.append(node)
    if node == goal:
        print("Path to goal:", path)
        return True
    if limit <= 0:
        return False
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, limit - 1, path.copy()):
            return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

found = dls(graph, 'A', 'F', limit=3)
if not found:
    print("Goal not found within depth limit")
