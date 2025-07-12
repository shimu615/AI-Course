from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        print("Start is the same as goal.")
        return [start]

    # Forward search (start -> goal)
    start_queue = deque([[start]])
    start_visited = {start}

    # Backward search (goal -> start)
    goal_queue = deque([[goal]])
    goal_visited = {goal}

    while start_queue and goal_queue:
        # Forward direction exploration
        path_from_start = start_queue.popleft()
        node_from_start = path_from_start[-1]

        # Check if node from start meets a node from goal
        if node_from_start in goal_visited:
            return path_from_start + list(reversed(goal_queue.popleft()))

        for neighbor in graph.get(node_from_start, []):
            if neighbor not in start_visited:
                start_visited.add(neighbor)
                start_queue.append(path_from_start + [neighbor])

        # Backward direction exploration
        path_from_goal = goal_queue.popleft()
        node_from_goal = path_from_goal[-1]

        # Check if node from goal meets a node from start
        if node_from_goal in start_visited:
            return list(reversed(start_queue.popleft())) + path_from_goal

        for neighbor in graph.get(node_from_goal, []):
            if neighbor not in goal_visited:
                goal_visited.add(neighbor)
                goal_queue.append(path_from_goal + [neighbor])

    print("No path found.")
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

path = bidirectional_search(graph, 'A', 'F')
print("Path found:", path)
