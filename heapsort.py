# import math
import sys
import random


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp



def heapify(A):
    for heap_index in range(1, len(A)):
        current = heap_index
        parent = int(heap_index / 2)
        while parent > 0 and A[current - 1] > A[parent - 1]:
            swap(A, parent-1, current-1)
            current = parent
            parent = int(parent / 2)
    return A


def heapsort(A):
    heapify(A)
    for i in range(len(A)):
        # heapify(A)
        # end = len(A) - 1 - i
        # swap(A, 0, end)
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

# print heapsort(crap)
printHeap(heapify(crap))