from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    while not pq.empty():
        _, current = pq.get()
        if current in visited:
            continue
        print("Visiting:", current)
        visited.add(current)
        if current == goal:
            print("Reached the goal!")
            return
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0  # Goal node
}

best_first_search(graph, 'A', 'F', heuristic)
