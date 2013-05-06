# Implement a set using an unbalanced binary search tree
#
# Additionally provide a random access function

class BST(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data > self.data:
            self.right = self.right and self.right.insert(data) or BST(data)
        else:
            self.left = self.left and self.left.insert(data) or BST(data)
        return self

    def find(self, data):
        if data == self.data:
            return self
        elif data > self.data and self.right:
            return self.right.find(data)
        elif self.left:
            return self.left.find(data)
        return None


class BSTSet(object):
    def __init__(self):
        self.bst = BST(None)

    def insert(self, data):
        if not self.bst.data:
            self.bst.data = data
        else:
            self.bst.insert(data)

    def contains(self, data):
        return bool(self.bst.find(data))

    def get(self, index):
        for i, data in enumerate(self.inorder()):
            if i == index:
                return data

    def inorder(self):
        current = self.bst
        stack = []
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                yield current.data
                current = current.right

    def preorder(self):
        stack = [self.bst]
        while len(stack) > 0:
            curr = stack.pop()
            if curr is not None:
                yield curr.data
                stack.append(curr.right)
                stack.append(curr.left)









s = BSTSet()
s.insert(10)
s.insert(5)
s.insert(15)
s.insert(1)
s.insert(6)
s.insert(11)
s.insert(50)
assert(s.get(2) == 6)
