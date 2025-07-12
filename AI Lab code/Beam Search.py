def beam_search(graph, start, goal, beam_width):
    frontier = [[start]]  # Initial frontier contains the start node
    while frontier:
        # Get the next set of paths in the frontier
        next_frontier = []
        for path in frontier:
            node = path[-1]
            if node == goal:
                print("Path to goal:", path)
                return path
            for neighbor in graph.get(node, []):
                next_frontier.append(path + [neighbor])

        # Sort paths by heuristic value and keep the top 'beam_width' paths
        next_frontier.sort(key=lambda x: len(x))  # Use length or other heuristic
        frontier = next_frontier[:beam_width]  # Keep only the top 'beam_width' paths

    print("Goal not found")
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

beam_width = 2
beam_search(graph, 'A', 'F', beam_width)
