from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    # Queue stores: (heuristic, node, accumulated_cost)
    pq.put((heuristic[start], start, 0))

    path = []

    while not pq.empty():
        _, current, current_cost = pq.get()

        if current in visited:
            continue

        path.append(current)
        visited.add(current)

        if current == goal:
            print(f"Goal Reached with total cost: {current_cost}")
            return path, current_cost

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, current_cost + cost))

    print("Goal not found.")
    return path, 0

graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('C', 1), ('D', 2)],
    'B': [('E', 1), ('F', 2)],
    'C': [], 'D': [('G', 1)],
    'E': [], 'F': [], 'G': []
}
heuristic = { 'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 1, 'E': 4, 'F': 5, 'G': 0 }

path, total_cost = best_first_search(graph, 'S', 'G', heuristic)
print(f"Path traversed: {path}")
print(f"Total Cost: {total_cost}")