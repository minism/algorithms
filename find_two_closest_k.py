# Given an unsorted array of floating point numbers and some value K
# within the same range as the array, find the pair of numbers in the array
# whose sum is closest to K

# n log n + n = O(n log n)


import random
import sys

lower, upper = -100, 100
K = random.randint(lower, upper)
A = [(random.random() * upper * 2) + lower for n in range(100)]


S = sorted(A)  # O(n log n)
back = 0
front = len(S) - 1
best_pair, best = (None, None), sys.maxint
while back < front:
    val = S[back] + S[front] - K
    if abs(val) < best:
        best = abs(val)
        best_pair = (S[back], S[front])
    if val > 0:
        front -= 1
    elif val < 0:
        back += 1
    else:
        break

print best_pair, K
