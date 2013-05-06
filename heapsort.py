# import math
import sys
import random


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def sift(A, start, end):
    # Repeatedly swap with smaller child to preserve min-heap
    curr = start
    while curr * 2 + 1 <= end:
        child = curr * 2 + 1
        to_swap = curr
        if A[child] > A[curr]:
            to_swap = child
        if child + 1 <= end and A[child + 1] > A[to_swap]:
            to_swap = child + 1
        if to_swap == curr:
            return  # Done
        swap(A, curr, to_swap)
        curr = to_swap


def heapify(A):
    # Start at last parent index
    size = len(A) - 1
    i = (size - 1) / 2
    while i >= 0:
        sift(A, i, size)
        i -= 1
    return A


def heapsort(A):
    heapify(A)
    size = len(A)
    for i in range(size):
        sortIndex = size - i - 1
        swap(A, 0, sortIndex)
        sift(A, 0, sortIndex - 1)
    return A


def printHeap(heap, items=[1], level=1):
    width = len(heap) * 2
    spacing = width / 2 ** level
    next = []
    for item in items:
        sys.stdout.write(' ' * spacing)
        sys.stdout.write(str(heap[item - 1]))
        if item * 2 < len(heap):
            next.append(item * 2)
        if item * 2 + 1 < len(heap):
            next.append(item * 2 + 1)
    sys.stdout.write('\n')
    if len(next) > 0:
        printHeap(heap, next, level=level+1)



crap = [random.randint(0, 100) for n in range(8)]

printHeap(heapify(crap))
print
print heapsort(crap)