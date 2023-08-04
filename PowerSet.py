# CS 325
# Homework #4 Part 1

def powerset_helper(pointer, choices_made, inputSet, result):
    if(pointer < 0):
        result.append(sorted(choices_made.copy()))
        return
    
    choices_made.append(inputSet[pointer])
    powerset_helper(pointer - 1, choices_made, inputSet, result)
    # Backtracking
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, inputSet, result)
    
def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    return result

if __name__ == "__main__":
    # Should return [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    print(powerset([1, 2, 3]))
    
    # Should return [[]]
    print(powerset([]))
    
    # Should return [[1, []]
    print(powerset([1]))
    
    # Should return [[1, 2], [2], [1], []]
    print(powerset([1, 2]))
    
    # Should return [[1, 2, 3, 4], [2, 3, 4], [1, 3, 4], [3, 4], [1, 2, 4], [2, 4], [1, 4], [4], [1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
    print(powerset([1, 2, 3, 4]))
    