import heapq

# # Input will be in format of:
# puzzle = [
#     ['-', '-', '-', '-', '-'],
#     ['-', '-', '#', '-', '-'],
#     ['-', '-', '-', '-', '-'],
#     ['#', '-', '#', '#', '-'],
#     ['-', '#', '-', '-', '-']
# ]
# calling_func = solve_puzzle(puzzle, (0, 0), (4,4))

# Output will be in format of:
# ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')


EMPTY = '-'
BARRIER = '#'           # Unused, just added for context

def valid_helper(Board, x, y):
    M = len(Board)
    N = len(Board[0])
    # Checks if in the bounds of the board and if the spot is EMPTY
    if 0 <= x < M and 0 <= y < N and Board[x][y] == EMPTY:
        return True
    return False

MOVES = [(0, 1, 'R'), 
        (0, -1, 'L'), 
        (1, 0, 'D'), 
        (-1, 0, 'U')]

def solve_puzzle(Board, source, destination):
    queue = [(0, source, [source], '')]  # Priority queue (path length, position, path)
    visited = set()
    
    while queue:
        path_len, (x, y), path, directions = heapq.heappop(queue)
        if (x, y) == destination:
            # Then we found the destination!
            return path, directions
    
        if (x, y) not in visited:
            visited.add((x, y))
            
            # For each possible move available
            for dx, dy, direction in MOVES:
                new_x, new_y = x + dx, y + dy
                
                # If valid and not yet visited
                if valid_helper(Board, new_x, new_y) and (new_x, new_y) not in visited:
                    new_path = path + [(new_x, new_y)]
                    new_path_len = path_len + 1
                    new_directions = directions + direction
                    heapq.heappush(queue, (new_path_len, (new_x, new_y), new_path, new_directions))
    
    # Then there is non valid path to the destination            
    return None, None

if __name__ == "__main__":
    puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
    ]

    source1 = (0, 2)
    destination1 = (2, 2)
    result1 = solve_puzzle(puzzle, source1, destination1)
    print(result1)  # Correct Output: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
    
    
    source2 = (0,0)
    destination2 = (4,4)
    result2 = solve_puzzle(puzzle, source2, destination2)
    print(result2)  # Correct Output: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    
    source3 = (0,0)
    destination3 = (4,0)
    result3 = solve_puzzle(puzzle, source3, destination3)
    print(result3)  # Correct Output: None        (No possible solution)    
    