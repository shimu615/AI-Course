class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
        self.status = {}      # Track status (solved or not)
        self.solution = {}    # Final solution path

    def ao_star(self, node, backtracking=False):
        print(f"Visiting Node: {node}")
        if node not in self.graph:
            self.status[node] = 'solved'
            return self.heuristic[node]

        min_cost = float('inf')
        best_path = None

        for child_set in self.graph[node]:
            cost = 0
            for child in child_set:
                cost += self.heuristic.get(child, 0)
            if cost < min_cost:
                min_cost = cost
                best_path = child_set

        self.heuristic[node] = min_cost
        self.solution[node] = best_path

        for child in best_path:
            self.ao_star(child, True)

        self.status[node] = 'solved'
        if not backtracking:
            self.display_solution()

        return self.heuristic[node]

    def display_solution(self):
        print("\nOptimal Solution Path:")
        for k in self.solution:
            print(f"{k} -> {self.solution[k]}")

graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E', 'F']],
    'C': [['G']],
    'D': [['H']],
    'E': [], 'F': [], 'G': [], 'H': []
}

heuristic = {
    'A': 0, 'B': 1, 'C': 2, 'D': 4,
    'E': 5, 'F': 6, 'G': 2, 'H': 3
}

g = Graph(graph, heuristic)
g.ao_star('A')
