# Generate random integers given an array of integer weights
#
# http://www.careercup.com/question?id=17433662


import random


def weighted_random(W):
    r = random.random()
    weight_sum = float(sum(W))
    last_theta = 0
    for i, weight in enumerate(W):
        theta = last_theta + (weight / weight_sum)
        if r <= theta:
            return i
        last_theta = theta


print weighted_random([1,2,1,2,1])
