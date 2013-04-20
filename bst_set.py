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
        # Random access on ordered set.  Perform in-order DFS on BST
        # stack = [self.bst]
        # while len(stack) > 0:
        pass

    def inorder(self):
        # In order generator for the bst
        parents = []
        node = self.bst
        while len(parents) > 0 or node is not None:
            while node.left:
                parents.append(node)
                node = node.left
            print node.data
            if node.right:
                parents.append(node)
                node = node.right


        # node = node or self.bst
        # if node.left:
        #     self.inorder(node=node.left)
        # print node.data
        # if node.right:
        #     self.inorder(node=node.right)

        return None







s = BSTSet()
s.insert(20)
s.insert(1)
s.insert(30)
s.insert(6)
s.insert(-5)
s.insert(2)

print(list(s.inorder()))
