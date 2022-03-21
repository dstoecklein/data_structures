from typing import Any

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None


class BT:
    def __init__(self) -> None:
        self.root = None # type: Node


    def _preOrderTraversal(self, node: Node) -> None:
        if node is not None:
            print(node.value)
            self._preOrderTraversal(node.left)
            self._preOrderTraversal(node.right)


    def _inOrderTraversal(self, node: Node) -> None:
        if node is not None:
            self._inOrderTraversal(node.left)
            print(node.value)
            self._inOrderTraversal(node.right)


    def _postOrderTraversal(self, node: Node) -> None:
        if node is not None:
            self._postOrderTraversal(node.left)
            self._postOrderTraversal(node.right)
            print(node.value)


    def _insert(self, node: Node, value: Any) -> None:
        if value <= node.value: # left insert
            if node.left is None:
                node.left = Node(value=value)
            else:
                self._insert(node=node.left, value=value)
        else: # right insert
            if node.right is None:
                node.right = Node(value=value)
            else:
                self._insert(node=node.right, value=value)
        

    def _getMinNode(self, node: Node) -> Node:
        curr = node
        while(curr.left is not None):
            curr = curr.left
        return curr


    def _getMaxNode(self, node: Node) -> Node:
        curr = node
        while(curr.right is not None):
            curr = curr.right
        return curr


    def _deleteNode(self, node: Node, value: Any) -> Node:
        if node is None:
            return node

        if value < node.value:
            node.left = self._deleteNode(node=node.left, value=value)
        elif value > node.value:
            node.right = self._deleteNode(node=node.right, value=value)
        else:
            if node.left is None:
                tmp = node.right
                node = None
                return tmp
            elif node.right is None:
                tmp = node.left
                node = None
                return tmp

            tmp = self._getMinNode(node=node.right)
            node.value = tmp.value
            node.right = self._deleteNode(node=node.right, value=tmp.value)
        return node


    def preOrderTraversal(self) -> None:
        if self.root is not None:
            self._preOrderTraversal(node=self.root)
        else:
            return "Binary Tree does not exist!"


    def inOrderTraversal(self) -> None:
        if self.root is not None:
            self._inOrderTraversal(node=self.root)
        else:
            return "Binary Tree does not exist!"


    def postOrderTraversal(self) -> None:
        if self.root is not None:
            self._postOrderTraversal(node=self.root)
        else:
            return "Binary Tree does not exist!"


    def insert(self, value) -> None:
        if self.root is not None:
            self._insert(node=self.root, value=value)
        else: # root insert
            self.root = Node(value=value)


    def getMinNode(self) -> Node:
        if self.root is not None:
            return self._getMinNode(node=self.root)
        else:
            return None


    def getMaxNode(self) -> Node:
        if self.root is not None:
            return self._getMaxNode(node=self.root)
        else:
            return None


    def deleteNode(self, value: Any) -> None:
        if self.root is not None:
            self._deleteNode(node=self.root, value=value)
        else:
            return "Binary Tree does not exist!"

bt = BT()
bt.root = Node("N1")
bt.root.left = Node("N2")
bt.root.right = Node("N3")
bt.root.left.left = Node("N4")
bt.root.left.right = Node("N5")
bt.root.right.left = Node("N6")
bt.root.right.right = Node("N7")

bt.preOrderTraversal()
print("===")
bt.inOrderTraversal()
print("===")
bt.postOrderTraversal()
print("===insert===")

bt2 = BT()
bt2.insert(10)
bt2.insert(5)
bt2.insert(20)
bt2.insert(2)
bt2.insert(7)
bt2.insert(15)
bt2.insert(30)

bt2.preOrderTraversal()
print("===")
bt2.inOrderTraversal()
print("===")
bt2.postOrderTraversal()
print("===Min/Max===")
print(bt2.getMinNode())
print(bt2.getMaxNode())
print("===Delete===")
bt2.deleteNode(value=30)
bt2.preOrderTraversal()