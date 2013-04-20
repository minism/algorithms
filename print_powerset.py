def powerset_rec(L):
    if len(L) < 1:
        return [[]]
    return [L[0] + subset for subset in powerset_rec(L[1:])]


def print_powerset_rec(L):
    print powerset_rec(L)


def print_powerset_nonrec(L):
    stack = L[:]
    powerset = [[]]
    while len(stack) > 0:
        item = stack.pop()
        new = []
        for existing in powerset:
            new.append([item] + existing)
        powerset.extend(new)
    print powerset


A = ['a', 'b', 'c', 'd']
# print_powerset_nonrec(A)
print_powerset_rec(A)