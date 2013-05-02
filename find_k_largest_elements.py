# Find k largest elements in an array
#
# http://www.careercup.com/question?id=17693675
#
#
# Perform quick select to get kth element, and find all elements larger


import random


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def qselect(A, k, left=None, right=None):
    left = left or 0
    right = right = len(A) - 1
    pivot = random.randint(left, right)
    pivotVal = A[pivot]

    # Move pivot out of the sorting range
    swap(A, pivot, right)
    swapIndex, i = left, left
    while i <= right - 1:
        if A[i] < pivotVal:
            swap(A, i, swapIndex)
            swapIndex += 1
        i += 1
    # Move pivot to final position
    swap(A, right, swapIndex)

    # Check if pivot matches, else recurse on the correct half
    rank = len(A) - swapIndex
    if k == rank:
        return A[swapIndex]
    elif k < rank:
        return qselect(A, k, left=swapIndex+1, right=right)
    else:
        return qselect(A, k, left=left, right=swapIndex-1)
        

def find_largest(A, k):
    kth_largest = qselect(A, k)
    result = []
    for item in A:
        if item >= kth_largest:
            result.append(item)
    return result


print find_largest(range(100), 10)
