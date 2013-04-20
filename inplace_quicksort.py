import random

def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

def qsort(A, left=None, right=None):
	left = left or 0
	right = right or len(A) - 1

	if left < right:
		pivot = random.randint(left, right)
		pivot_value = A[pivot]
		swap(A, pivot, right)
		swap_index = left
		for i in range(left, right):
			if A[i] < pivot_value:
				swap(A, i, swap_index)
				swap_index += 1
		swap(A, right, swap_index)

		qsort(A, left=left, right=swap_index-1)
		qsort(A, left=swap_index+1, right=right)

	return A


print qsort([random.choice(range(100)) for n in range(100)])