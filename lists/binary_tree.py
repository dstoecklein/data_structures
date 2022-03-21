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

from lists.queue import LinkedListQueue  # type: ignore


# Binary Tree using Custom queue
class CustomQueueBinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        return f"{self.data}"

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

    def levelOrderTraversal(self, root):
        if not root:
            return
        queue = LinkedListQueue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            print(root.data.data)
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            if root.data.right is not None:
                queue.enqueue(root.data.right)

    def search(self, root, data):
        if not root:
            return "Binary Tree does not exist!"
        # use level order traversal because it uses queue = better
        queue = LinkedListQueue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.data.data == data:
                return root.data
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            if root.data.right is not None:
                queue.enqueue(root.data.right)
        return None

    def insert(self, root, new):
        if not root:
            root = new
        queue = LinkedListQueue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            else:
                root.data.left = new
                return
            if root.data.right is not None:
                queue.enqueue(root.data.right)
            else:
                root.data.right = new
                return

    def getDeepestNode(self, root):
        if not root:
            return
        queue = LinkedListQueue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            if root.data.right is not None:
                queue.enqueue(root.data.right)
        deepestNode = root.data
        return deepestNode

    def deleteDeepestNode(self, root):
        if not root:
            return
        deepestNode = self.getDeepestNode(root)
        queue = LinkedListQueue()
        queue.enqueue(root)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.data is deepestNode:  # root
                root.data = None
                return
            if root.data.right:  # right
                if root.data.right is deepestNode:
                    root.data.right = None
                    return
                else:
                    queue.enqueue(root.data.right)
            if root.data.left:  # left
                if root.data.left is deepestNode:
                    root.data.left = None
                    return
                else:
                    queue.enqueue(root.data.left)


tree = CustomQueueBinaryTree(2)

left = CustomQueueBinaryTree(3)
right = CustomQueueBinaryTree(4)

left2 = CustomQueueBinaryTree(5)
right2 = CustomQueueBinaryTree(6)

tree.left = left
tree.left.left = left2
tree.left.right = right2

tree.right = right

tree.preOrderTraversal(tree)
print("===")
tree.inOrderTraversal(tree)
print("===")
tree.postOrderTraversal(tree)
print("===")
tree.levelOrderTraversal(tree)
print("===")
print(tree.search(tree, 5).data)
print("===")
new_node = CustomQueueBinaryTree(7)
tree.insert(tree, new_node)
print("===")
tree.levelOrderTraversal(tree)
print("===")
print(tree.getDeepestNode(tree))
print("===")
tree.deleteDeepestNode(tree)
tree.levelOrderTraversal(tree)


# BT using Python list (better)
# [none, root, left, right, lleft, lright, rleft, rright, llleft, llright, ...]
class PythonListBinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, data):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is full!"
        self.customList[self.lastUsedIndex + 1] = data
        self.lastUsedIndex += 1
        return

    def searchNode(self, nodeData):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeData:
                return self.customList[i]  # found
        return None

    def preOrderTraversal(self, idx):
        if idx > self.lastUsedIndex:
            return
        print(self.customList[idx])
        self.preOrderTraversal(idx * 2)
        self.preOrderTraversal(idx * 2 + 1)

    def inOrderTraversal(self, idx):
        if idx > self.lastUsedIndex:
            return
        self.preOrderTraversal(idx * 2)
        print(self.customList[idx])
        self.preOrderTraversal(idx * 2 + 1)

    def postOrderTraversal(self, idx):
        if idx > self.lastUsedIndex:
            return
        self.preOrderTraversal(idx * 2)
        self.preOrderTraversal(idx * 2 + 1)
        print(self.customList[idx])

    def levelOrderTraversal(self, idx):
        for i in range(idx, self.lastUsedIndex + 1):
            print(self.customList[i])


print("=======")
bt = PythonListBinaryTree(8)
bt.insertNode(5)
bt.insertNode(6)
bt.insertNode(7)
bt.insertNode(2)
print(bt.searchNode(1))
bt.preOrderTraversal(0)
