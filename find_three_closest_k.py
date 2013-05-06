# Given an unsorted array of floating point numbers and some value K
# within the same range as the array, find a set of three numbers
# whose sum is closest to K

# n log n + n^2 = O(n^2)

import random

def find_three_closest_k(A, k=0):
    # Begin with n log n sort of array
    A = sorted(A)

    # For each element in A, perform the find_two algorithm
    best = None
    best_set = None
    for i in range(len(A) - 2):
        front, back = i + 1, len(A) - 1
        while front < back:
            value = A[front] + A[back] + A[i] - k
            if best == None or abs(value) < best:
                best = abs(value)
                best_set = (A[front], A[back], A[i])
            if value < k:
                front += 1
            elif value > k:
                back -= 1
            else:
                # sum == k!
                break

    return best_set




lower, upper = -100, 100

# A = [(random.random() * upper * 2) + lower for n in range(100)]
A = [-7, -50, -20, 32, 9, 4, 3, 10]
print find_three_closest_k(A, k=0)

