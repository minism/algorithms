import string
import random

class LzwTable(list):
	def __init__(self):
		self.append(' ')
		for char in string.uppercase:
			self.append(char)


def lzw_compress(input):
	table = LzwTable()
	output = []
	i = 0
	while i < len(input):
		j = i + 1
		while j <= len(input):
			substr = ''.join(input[i:j])
			if substr not in table:
				output.append(table.index(last_sub))
				table.append(substr)
				break
			last_sub = substr
			j = j + 1
		i = j - 1
	return output


def lzw_decompress(input):
	table = LzwTable()
	output = []
	for i in range(len(input)):
		code = input[i]
		curr = table[code]
		if i < len(input) - 1:
			next = curr + table[input[i+1]][0]
			table.append(next)
		output.append(curr)
	return output


size = 5000
# input = [random.choice(string.uppercase) for i in range(size)]
input = list('TOBEORNOTTOBEORTOBEORNOT')

compressed = lzw_compress(input)
print "%s%% compressed" % ((1 - float(len(compressed)) / len(input)) * 100)

assert(''.join(input) == ''.join(lzw_decompress(compressed)))

