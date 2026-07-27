from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()

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
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('Z', 10)],
    'C': [('Z', 3)],
    'Z': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'Z': 0
}

path, total_cost = best_first_search(graph, 'A', 'Z', heuristic)
print(f"Path traversed: {path}")
print(f"Total Cost: {total_cost}")