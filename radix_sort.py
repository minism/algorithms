import random


def getdigit(num, pos):
    return num / 10 ** pos % 10


def rsort(L, dindex=0):
    buckets = {}
    for digit in range(10):
        buckets[digit] = []

    finished = True
    for number in L:
        digit = getdigit(number, dindex)
        buckets[digit].append(number)
        if digit > 0:
            finished = False

    ret = []
    for digit in range(10):
        ret.extend(buckets[digit])

    if not finished:
        return rsort(ret, dindex=dindex+1)
    return ret





ints = [random.randint(0, 1000) for n in range(1000)]
print rsort(ints)
