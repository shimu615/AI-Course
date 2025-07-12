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

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit: {depth}")
        if dls(graph, start, goal, depth):
            return
    print("Goal not found within depth limit")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

ids(graph, 'A', 'F', max_depth=4)
