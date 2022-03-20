# Every node in a binary tree can only have 2 children (left, right)
# Binary Tree is a family of data structures
#   (BST, Heap Tree, AVL, ...)
# Binary Tree Types:
#   Full Binary Tree: Every Node has 2 or 0 childs, not 1
#   Perfect Binary Tree: All Leaf Node has 2 childs
#   Complete Binary Tree: All levels are filled, except last level
#   Balanced Binary Tree: All leaf nodes are distanced from root in same distance
# Binary Tree represantation:
#   Linked List
#   Python List

import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def preOrderTraversal(self, root):
        if not root:
            return
        # root -> left -> right
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root):
        if not root:
            return
        # left -> root -> right
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if not root:
            return
        # left -> right -> root
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)

    def search(root, data):
        if not root:
            return "Binary Tree does not exist!"
        

tree = Node(2)
left = Node(3)
right = Node(4)

tree.left = left
tree.right = right

tree.preOrderTraversal(tree)
print("===")
tree.inOrderTraversal(tree)
print("===")
tree.postOrderTraversal(tree)