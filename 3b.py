from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    # Cost, current_node, path
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

graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)]
}
heuristic = { 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0, 'S': 5}

path, cost = a_star_search(graph, 'S', 'G', heuristic)
print("A* Path:", path)
print("Total Cost:", cost)