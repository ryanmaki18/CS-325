# CS 325
# Homework #4 Part 1

def max_independent_set(nums):
    
    # initilzizing list and base case
    nums_len = len(nums)
    if nums_len == 0:
        return []
    
    # All negative case
    if all(num < 0 for num in nums):
        return []
    
    dp = [0] * (nums_len + 1)
    dp[1] = max(0, nums[nums_len - 1])
    
    for i in range(2, nums_len + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + max(0, nums[nums_len - i]))
        
    # Start at the end of the list and work to the front
    result = []
    index = nums_len
    while index >= 1:
        if dp[index] == dp[index - 1]:
            index -= 1
        else:
            result.append(nums[nums_len - index])
            index -= 2
            
    if dp[nums_len] == 0:
        return [0]
    else:
        return result 


if __name__ == "__main__":
    # Should return [7, 5, 6]
    print(max_independent_set([7, 2, 5, 8, 6]))
    
    # Should return [0]
    print(max_independent_set([-1, -1, 0]))
    
    # Should return []
    print(max_independent_set([-1, -1, -10, -34]))
    
    # Should return [2, 4, 6, 8]
    print(max_independent_set([1, 2, 3, 4, 5, 6, 7, 8]))
    
    # Should return [8, 6, 4, 2]
    print(max_independent_set([8, 7, 6, 5, 4, 3, 2, 1 ]))
    
    # Should return [1, 1, 100, 1, 1]
    print(max_independent_set([1, 1, 1, 10, 100, 10, 1, 1, 1]))