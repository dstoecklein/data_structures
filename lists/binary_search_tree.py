class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return self._repr(self.root)

    def _repr(self, node, indent=0):
        string = ("\t" * indent) + str(node.data) + "\n"
        if node.left:
            string += ("\t" * (indent + 1)) + "Left:\n"
            string += self._repr(node.left, indent + 1)
        if node.right:
            string += ("\t" * (indent + 1)) + "Right:\n"
            string += self._repr(node.right, indent + 1)
        return string

    def _insert(self, root, value):
        if value <= root.data:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert(root.right, value)

    def _find(self, root, value):
        if value == root.data:
            return root
        elif value < root.data and root.left is not None:
            return self._find(root.left, value)
        elif value > root.data and root.right is not None:
            return self._find(root.right, value)

    def find(self, value):
        if self.root is None:
            return None
        return self._find(self.root, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)


bst = BST()
bst.insert(10)
bst.insert(60)
bst.insert(5)
bst.insert(20)

print(bst)
