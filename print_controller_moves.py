# http://www.careercup.com/question?id=15542726

import string

rows = 6
cols = 5


def rec(target, cursor):
    trow, tcol = target / cols, target % cols
    crow, ccol = cursor / cols, cursor % cols
    if trow < crow:
        print 'U'
        return rec(target, cursor - cols)
    elif trow > crow:
        print 'D'
        return rec(target, cursor + cols)
    elif tcol < ccol:
        print 'L'
        return rec(target, cursor - 1)
    elif tcol > ccol:
        print 'R'
        return rec(target, cursor + 1)
    else:
        print '!'
    return cursor

def print_moves(word):
    cursor = 0
    for char in word:
        target = ord(char) - 97
        cursor = rec(target, cursor)




print_moves('hi man whats up')