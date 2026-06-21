import random

def objective_function(x):
    # Example objective function: f(x) = -x^2 + 4x (parabola facing down, max at x=2)
    return -x**2 + 4*x

def get_neighbors(state, step_size=0.1):
    return [state - step_size, state + step_size]

def hill_climbing(start_state, max_iterations=1000):
    current_state = start_state
    current_value = objective_function(current_state)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_state)
        
        # Evaluate neighbors
        neighbor_evals = [(neighbor, objective_function(neighbor)) for neighbor in neighbors]
        
        # Find best neighbor
        best_neighbor, best_value = max(neighbor_evals, key=lambda x: x[1])
        
        # If no neighbor is better than current, we reached a peak
        if best_value <= current_value:
            break
            
        current_state, current_value = best_neighbor, best_value
        
    return current_state, current_value

start = random.uniform(-10, 10)
best_state, best_val = hill_climbing(start)
print(f"Starting state: {start:.4f}")
print(f"Local maximum found at x = {best_state:.4f}")
print(f"Objective value: {best_val:.4f}")
