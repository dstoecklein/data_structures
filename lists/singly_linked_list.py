from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

    def __eq__(self, other):
        if other is not None:
            return self.data == other.data and self.next == other.next
        return None


class SinglyLinkedList:
    def __init__(self, init_data=None):
        self.head = None
        self.tail = None
        self.length = 0  # type: int
        self.nodes = list()  # type: List[Node]

        if init_data:
            for data in init_data:
                self.insert_end(data)

    def __node_iter(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __iter__(self):
        """:returns values iterator"""
        return iter(map(lambda node: node.data, self.__node_iter()))

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __len__(self):
        return self.length

    def _add_node(self, node):
        self.nodes.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node is None:
            return None

        if node in self.nodes:
            self.nodes.remove(node)
            self.length -= 1
        else:
            raise RuntimeError("Node not in list!")

    def get_nth(self, n):
        temp_head = self.head
        counter = 1
        while temp_head is not None:
            if counter == n:
                return temp_head
            temp_head = temp_head.next
            counter += 1
        return None

    def get_nth_back(self, n):
        if self.length < n:
            return None
        return self.get_nth(self.length - n + 1)

    def insert_end(self, data):
        node = Node(data)
        self._add_node(node)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_front(self, data):
        node = Node(data)
        self._add_node(node)

        node.next = self.head
        self.head = node

        if self.length == 1:
            self.tail = self.head

    def insert_sorted(self, data):
        if not self.length or data <= self.head.data:
            self.insert_front(data)
        elif self.tail.data <= data:
            self.insert_end(data)
        else:
            prev = None
            curr = self.head
            while curr is not None:
                if curr.data >= data:
                    node = Node(data)
                    self._add_node(node)
                    node.next = curr
                    prev.next = node
                    break
                prev = curr
                curr = curr.next

    def delete_front(self):
        temp_next = self.head.next
        self._delete_node(temp_next)

        self.head = temp_next
        if self.length <= 1:
            self.tail = self.head

    def delete_end(self):
        if self.length <= 1:
            self.delete_front()
            return
        prev = self.get_nth(self.length - 1)

        self._delete_node(self.tail)
        self.tail = prev
        self.tail.next = None

    def delete_with_key(self, data):
        if not self.length:
            return

        if self.head.data == data:
            self.delete_front()
        else:
            curr = self.head
            prev = None

            while curr is not None:
                if curr.data == data:
                    if curr == self.tail:
                        self.tail = prev
                    prev.next = curr.next
                    self._delete_node(curr)
                    break
                prev = curr
                curr = curr.next
