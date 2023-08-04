## CS325 Homework #2

def kthElement(Arr1, Arr2, k):
    return kthElementRecursion(Arr1, 0, len(Arr1), Arr2, 0, len(Arr2), k - 1)

def kthElementRecursion(Arr1, start1, end1, Arr2, start2, end2, k):
    size1 = end1 - start1
    size2 = end2 - start2

    if size1 == 0:
        return Arr2[start2 + k]
    if size2 == 0:
        return Arr1[start1 + k]
    if k == 0 or k == -1:
        return min(Arr1[start1], Arr2[start2])
    
    mid1 = (size1 * (start1 + size1 - end1)) // size1 
    mid2 = k - mid1 - 1

    if start1 + mid1 >= end1:
        mid1 = end1 - start1 - 1
        mid2 = k - mid1 - 1

    if start2 + mid2 >= end2:
        mid2 = end2 - start2 - 1
        mid1 = k - mid2 - 1

    if Arr1[start1 + mid1] <= Arr2[start2 + mid2]:
        return kthElementRecursion(Arr1, start1 + mid1 + 1, end1, Arr2, start2, end2, k - mid1 - 1)
    else:
        return kthElementRecursion(Arr1, start1, end1, Arr2, start2 + mid2 + 1, end2, k - mid2 - 1)



## ----------------------  FIXME: UNCOMMENT ALL PRINT STATEMENTS FOR TESTING!!!!! -------------------------------

if __name__ == '__main__':
    Arr1 = [1,2,3,5,6] ; Arr2= [3,4,5,6,7] ; k1= 5
    answer1 = kthElement(Arr1, Arr2, k1)
    ## print(answer1)
    # Returns: 4
    # Explanation: 5th element in the combined sorted array [1,2,3,3,4,5,5,6,6,7] is 4

    Arr3 = [1,2,3,5,6] ; Arr4= [3,4,5,6,7] ; k2= 1
    answer2 = kthElement(Arr3, Arr4, k2)
    ## print(answer2)
    # Returns: 1
    # Explanation: 1st element in the combined sorted array [1,2,3,3,4,5,5,6,6,7] is 1

    Arr5 = [1,2,3,5,6] ; Arr6= [3,4,5,6,7] ; k3= 0
    answer3 = kthElement(Arr5, Arr6, k3)
    ## print(answer3)
    # Returns: 1
    # Explanation: 0th element in the combined sorted array [1,2,3,3,4,5,5,6,6,7] is minimum of Arr5 and Arr6

    Arr7 = [1,2,3,5,6] ; Arr8= [3,4,5,6,7] ; k4 = 9
    answer4 = kthElement(Arr7, Arr8, k4)
    ## print(answer4)
    # Returns: 6
    # Explanation: 10th element in the combined sorted array [1,2,3,3,4,5,5,6,6,7] is 6

    Arr9 = [1,2,3,5,6] ; Arr10= [3,4,5,6,7] ; k5 = 10
    answer5 = kthElement(Arr9, Arr10, k5)
    ## print(answer5)
    # Returns: 7
    # Explanation: 5th element in the combined sorted array [1,2,3,3,4,5,5,6,6,7] is 7