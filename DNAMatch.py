# CS 325
# Homework #3 -- Ryan Maki

def dna_match_topdown(DNA1, DNA2):
    memo = {}
    return dna_match_topdown_helper(DNA1, DNA2, 0, 0, memo)

def dna_match_topdown_helper(DNA1, DNA2, i, j, memo):
    if i == len(DNA1) or j == len(DNA2):
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if DNA1[i] == DNA2[j]:
        memo[(i, j)] = 1 + dna_match_topdown_helper(DNA1, DNA2, i + 1, j + 1, memo)
    else:
        memo[(i, j)] = max(dna_match_topdown_helper(DNA1, DNA2, i + 1, j, memo), 
                           dna_match_topdown_helper(DNA1, DNA2, i, j + 1, memo))
    return memo[(i, j)]

def dna_match_bottomup(DNA1, DNA2):
    len1 = len(DNA1) + 1
    len2 = len(DNA2) + 1
    table = []
    for _ in range(len1):
        row = []
        for _ in range(len2):
            row.append(0)
        table.append(row)
        
    for i in range(len1):
        for j in range(len2):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[len1 - 1][len2 - 1]



if __name__ == "__main__":
    DNA1 = "ATAGTTCCGTCAAA"
    DNA2 = "GTGTTCCCGTCAAA"
    # print("Top-down:")
    # result1 = dna_match_topdown(DNA1, DNA2)
    # print(result1)
    
    # print("Bottom-up:")
    # result2 = dna_match_bottomup(DNA1, DNA2)
    # print(result2)
    
    DNA1 = "GACGTGACGACACT"
    DNA2 = "CTGATCGAGTCTAT"
    # print("Top-down:")
    # result1 = dna_match_topdown(DNA1, DNA2)
    # print(result1)
    
    # print("Bottom-up:")
    # result2 = dna_match_bottomup(DNA1, DNA2)
    # print(result2)
