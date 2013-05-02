# http://www.careercup.com/question?id=17850664

# Given N dice, each with A faces (can roll 1-A), and a sum S, determine number 
# of ways to sum S if all dice are rolled

import random


cache = {}
cache_hits = [0, 0]

def find_dice_combinations(dice, sum):
    # Try cache
    if cache.has_key((len(dice), sum)):
        cache_hits[0] += 1
        return cache.get((len(dice), sum))
    else:
        cache_hits[1] += 1

    num_combinations = 0
    if sum > 0 and len(dice) > 0:
        if len(dice) == 1:
            if 1 <= sum <= dice[0]:
                num_combinations = 1
        else:
            # Recurse for each roll of current die
            for i in range(dice[0]):
                roll = dice[0] - i
                num_combinations += find_dice_combinations(dice[1:], sum-roll)
            return num_combinations

    cache[(len(dice), sum)] = num_combinations
    return num_combinations


print find_dice_combinations([8]*8, 64)
print "%s cache hits, %s cache misses" % (cache_hits[0], cache_hits[1])