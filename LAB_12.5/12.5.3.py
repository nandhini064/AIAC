import random
import math

# Static sensor coordinates (x, y)
coords = [
    [69.65, 28.61], [22.69, 55.23], [87.56, 98.25], [68.46, 39.48],
    [66.50, 4.39], [8.78, 62.48], [89.38, 79.51], [14.61, 76.10],
    [78.05, 19.59], [74.63, 56.40], [5.09, 13.57], [34.72, 91.57],
    [45.90, 87.82], [91.31, 62.29], [32.61, 43.71], [32.06, 44.45],
    [12.83, 60.16], [22.61, 23.37], [7.48, 75.97], [58.86, 69.83]
]
num_sensors = len(coords)

def total_distance(path, coords):
    total = 0
    for i in range(len(path) - 1):
        total += math.hypot(coords[path[i]][0] - coords[path[i+1]][0], coords[path[i]][1] - coords[path[i+1]][1])
    total += math.hypot(coords[path[-1]][0] - coords[path[0]][0], coords[path[-1]][1] - coords[path[0]][1])
    return total

def greedy_route(coords):
    n = len(coords)
    unvisited = set(range(n))
    route = [0]
    unvisited.remove(0)
    while unvisited:
        last_node = route[-1]
        next_city = min(unvisited, key=lambda city: math.hypot(coords[last_node][0] - coords[city][0], coords[last_node][1] - coords[city][1]))
        route.append(next_city)
        unvisited.remove(next_city)
    return route

def simulated_annealing(coords, initial_route, T=1000, alpha=0.995, stopping_T=1e-8, max_iter=10000):
    current_route = initial_route[:]
    current_distance = total_distance(current_route, coords)
    best_route = current_route[:]
    best_distance = current_distance
    n = len(coords)
    iter_count = 0
    while T > stopping_T and iter_count < max_iter:
        i, j = sorted(random.sample(range(n), 2))
        new_route = current_route[:i] + current_route[i:j+1][::-1] + current_route[j+1:]
        new_distance = total_distance(new_route, coords)
        
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / T):
            current_route = new_route
            current_distance = new_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance
        T *= alpha
        iter_count += 1
    return best_route

def compare_solutions(random_route, greedy_route, sa_route, coords):
    print("--- Sensor Route Optimization Comparison ---")
    
    random_dist = total_distance(random_route, coords)
    print(f"Random Route:       {random_dist:.2f} units")
    
    greedy_dist = total_distance(greedy_route, coords)
    print(f"Greedy Route:       {greedy_dist:.2f} units")
    
    sa_dist = total_distance(sa_route, coords)
    print(f"SA Optimized Route: {sa_dist:.2f} units")
    
    print("\n--- Improvement over Random Route ---")
    print(f"Greedy Improvement: {(1 - greedy_dist / random_dist) * 100:.2f}%")
    print(f"SA Improvement:     {(1 - sa_dist / random_dist) * 100:.2f}%")

if __name__ == "__main__":
    random_route = list(range(num_sensors))
    random.shuffle(random_route)
    
    greedy_route_path = greedy_route(coords)

    sa_optimized_route = simulated_annealing(coords, greedy_route_path)

    compare_solutions(random_route, greedy_route_path, sa_optimized_route, coords)