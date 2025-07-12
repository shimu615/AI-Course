# 🧠 AI Algorithm Implementations

This folder contains Python implementations of 10 core Artificial Intelligence algorithms taught in the AI course. Each algorithm includes example input/output and code-level explanations.

---

## 🔍 Implemented Algorithms:

1. **Breadth-First Search (BFS)**
   - **Purpose:** Explores all nodes at the present depth before moving to the next level.
   - **Applications:** Shortest path, social networks, web crawlers
   - **Time Complexity:** O(V + E)
     

2. **Depth-First Search (DFS)**
   - **Purpose:** Explores as far as possible along one branch before backtracking.
   - **Applications:** Cycle detection, maze solving, puzzle solving
   - **Time Complexity:** O(V + E)

3. **Depth-Limited Search (DLS)**
   - **Purpose:** DFS with a depth limit to avoid infinite loops
   - **Used In:** Game tree search with limited depth

4. **Iterative Deepening Search (IDS)**
   - **Purpose:** Combines DFS's space efficiency with BFS's completeness
   - **Application:** Resource-limited search systems

5. **Best-First Search**
   - **Purpose:** Uses heuristic to select the most promising node
   - **Used In:** Greedy algorithms

6. **Bidirectional Search**
   - **Purpose:** Runs two simultaneous searches from start and goal
   - **Benefits:** Reduces time complexity drastically

7. **Beam Search**
   - **Purpose:** Like BFS but with a fixed number of paths explored
   - **Used In:** Speech recognition, machine translation

8. **AND-OR Graph Search**
   - **Purpose:** Handles problems with multiple solution paths (AND/OR trees)
   - **Application:** Planning, non-deterministic AI problems

9. **Minimax Algorithm**
   - **Purpose:** Game theory algorithm for two-player games
   - **Application:** Chess, Tic Tac Toe, Checkers

10. **Alpha-Beta Pruning**
    - **Purpose:** Optimizes the Minimax algorithm by pruning unneeded branches
    - **Application:** Faster decision making in games

---

## 📁 File Structure

Each algorithm is stored in a separate `.py` file:

