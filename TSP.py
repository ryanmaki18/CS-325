# ------- Homework #7, Question #2 -------
# -------------- Ryan Maki --------------

def find_nearest_neighbor(curr_city, unvisited, G):
    nearest_neighbor = None
    neighbor_distance = 1000000000

    for city in unvisited:
        if G[curr_city][city] < neighbor_distance:
            if G[curr_city][city] != 0:
                nearest_neighbor = city
                neighbor_distance = G[curr_city][city]

    return nearest_neighbor

def solve_tsp(G):
    num_cities = len(G)
    unvisited = set(range(1, num_cities))
    path = []
    path.append(0)     # Starting at position 0
    curr_city = 0
    
    # While there are unvisited cities, find nearest city and add to path
    while unvisited:
        nearest_city = find_nearest_neighbor(curr_city, unvisited, G)
        path.append(nearest_city)
        unvisited.remove(nearest_city)
        curr_city = nearest_city
        
    # Returning to the city we started at, then return the path
    path.append(0)
    return path


if __name__=="__main__":
    G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
    ]

    result = solve_tsp(G)
    print("TSP Path:", result)
    