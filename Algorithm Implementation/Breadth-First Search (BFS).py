from collections import deque

def bfs(graph, start, goal):
    visited = set()                      # Visited nodes store kora hobe
    queue = deque([[start]])             # Start node diye queue suru
    while queue:
        path = queue.popleft()           # Path er last node check kori
        node = path[-1]
        if node in visited:              # Already visited hole skip
            continue
        visited.add(node)                # Visit kori
        if node == goal:                 # Goal pele print
            print("Path to goal:", path)
            return
        for neighbor in graph.get(node, []):  # Neighbors ghuri
            new_path = list(path)             # Notun path banai
            new_path.append(neighbor)
            queue.append(new_path)            # Queue te push kori

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A', 'F')
