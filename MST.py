
import heapq

# # Input will be in format of:
# input = [
#     [0, 8, 5, 0, 0, 0, 0],
#     [8, 0, 10, 2, 18, 0, 0],
#     [5, 10, 0, 3, 0, 16, 0],
#     [0, 2, 3, 0, 12, 30, 14],
#     [0, 18, 0, 12, 0, 0, 4],
#     [0, 0, 16, 30, 0, 0, 26],
#     [0, 0, 0, 14, 4, 26, 0]
# ]

# # Output will be in format of:
# """
# Result:
# [(0, 2, 5), (2, 3, 3), (3, 1, 2), (3, 4, 12), (4, 6, 4), (2, 5, 16)]
# """

def Prims(graph):
    result = []
    selected = [False] * len(graph)
    selected[0] = True               # Since we start at vertex 0
    min_heap = []
    
    # Initialize min_heap
    for i in range(1, len(graph)):
        if graph[0][i] > 0:
            heapq.heappush(min_heap, (graph[0][i], 0, i))


    while min_heap:
        weight, vertex1, vertex2 = heapq.heappop(min_heap)
        
        # If vertex2 is not yet a part of the tree, then add it
        if not selected[vertex2]:
            result.append((vertex1, vertex2, weight))
            selected[vertex2] = True
            
            # Looping through newly added vertex2 edge
            for i in range(len(graph)):
                if not selected[i] and graph[vertex2][i] > 0:
                    heapq.heappush(min_heap, (graph[vertex2][i], vertex2, i))
                    
    return result

# Example usage:
# if __name__ == "__main__":
    # input = [
    #     [0, 8, 5, 0, 0, 0, 0],
    #     [8, 0, 10, 2, 18, 0, 0],
    #     [5, 10, 0, 3, 0, 16, 0],
    #     [0, 2, 3, 0, 12, 30, 14],
    #     [0, 18, 0, 12, 0, 0, 4],
    #     [0, 0, 16, 30, 0, 0, 26],
    #     [0, 0, 0, 14, 4, 26, 0]
    # ]
    # output = Prims(input)
    # print("Result:")
    # print(output)
