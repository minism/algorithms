# Given an Array of strings, find the maximum common substring in all the strings

import random
import string


def find_max_sub(A):
    return A



strings = []
for i in range(100):
    strings.append(''.join([random.choice(string.lowercase) for j in range(random.randint(10, 30))]))

print find_max_sub(strings)