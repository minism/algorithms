# Given a function KNOWS(A,B), which returns 1 if A knows B 
# (and not necessarily the other way around) and 0 if A does not know B. 

# A Celebrity is one who does not know anyone, 
# and one who is known by everybody. 

# For a list of N people, find all celebrities in linear time.

import random


num_people = 100
people = dict(((i, {}) for i in range(num_people - 1)))
for person in people.values():
    person['knows'] = [random.choice(people.keys()) for i in range(random.randint(1, num_people - 1))]

# add celebrity
celeb_id = num_people - 1
people[celeb_id] = {'knows': []}
for person in people.values():
    person['knows'].append(celeb_id)


def knows(a, b):
    return b in people[a]['knows']


random.shuffle(people)

potential_celebs = people.keys()[:]
while len(potential_celebs) > 0:
    if len(potential_celebs) == 1:
        print "Done: celeb is %s" % potential_celebs[0]
    else:
        for i in range(len(potential_celebs)):
            for j in range(len(potential_celebs)):


