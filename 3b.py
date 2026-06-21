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
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)]
}
heuristic = { 'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0 }

path, cost = a_star_search(graph, 'S', 'G', heuristic)
print("A* Path:", path)
print("Total Cost:", cost)
