import sys

def find_max_subarray(L):
	table = [(-sys.maxint, 0)]
	for i in range(len(L)):
		curr = sum(L[0:i+1])
		if curr > table[0][0]:
			table[0] = (curr, i)

	best = 0
	for i in range(1, len(L)):
		table.append((table[i-1][0] - L[i-1], table[i-1][1]))
		if table[i][0] > table[best][0]:
			best = i




input = [10, 35, -5, -50, 40, 0]
print find_max_subarray(input)
