from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, start, [start]))

    while not pq.empty():
        _, g_cost, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g_cost

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_cost = g_cost + cost
                pq.put((new_cost + heuristic[neighbor], new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# Simple 4-node graph for exam
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

path, cost = a_star_search(graph, 'A', 'Z', heuristic)
print("A* Path:", path)
print("Total Cost:", cost)