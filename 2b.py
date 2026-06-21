from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    
    path = []
    
    while not pq.empty():
        _, current = pq.get()
        
        if current in visited:
            continue
            
        path.append(current)
        visited.add(current)
        
        if current == goal:
            print("Goal Reached!")
            return path
            
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
                
    print("Goal not found.")
    return path

# Example graph and heuristic
graph = {
    'S': [('A', 1), ('B', 2)],
    'A': [('C', 1), ('D', 2)],
    'B': [('E', 1), ('F', 2)],
    'C': [], 'D': [('G', 1)],
    'E': [], 'F': [], 'G': []
}
heuristic = { 'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 1, 'E': 4, 'F': 5, 'G': 0 }

path = best_first_search(graph, 'S', 'G', heuristic)
print("Path traversed:", path)
