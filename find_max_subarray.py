import sys

def find_max_subarray(L):
    best = None
    left, right = 0, 0
    total = 0
    for i in range(len(L)):
        total = total + L[i]
        if not best or total > best:
            best = total
            right = i
    total = best
    for i in range(right):
        total = total - L[i]
        if total > best:
            left = i+1
            best = total
    return L[left:right+1]




input = [40, 35, -5, -50, 60, 0]
print find_max_subarray(input)
