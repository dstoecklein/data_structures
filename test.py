class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f'{self.data}'

class LinkedList:
    def __init__(self, init_nodes) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        self.nodes = []

        if init_nodes:
            for node in init_nodes:
                self.insert_end(node)

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    def _add_node(self, node):
        self.nodes.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.length -= 1
        else:
            raise RuntimeError("Node not in list!")

    def _link(self, node1, node2):
        if node1:
            node1.next = node2
        if node2:
            node2.prev = node1

    def get_nth(self, n):
        curr = self.head
        counter = 1
        while curr is not None:
            if counter == n:
                return curr # return the node
            curr = curr.next
            counter += 1

    def insert_end(self, data):
        node = Node(data)
        self._add_node(node)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node

    def insert_front(self, data):
        node = Node(data)
        self._add_node(node)

        self._link(node, self.head)
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
                    self._link(node, curr)
                    self._link(prev, node)
                    break
                prev = curr
                curr = curr.next

    def delete_front(self):
        if not self.head:
            return

        new_head = self.head.next
        self._delete_node(self.head)
        self.head = new_head

        if self.length <= 1:
            self.tail = self.head

    def delete_end(self):
        if self.length <= 1:
            self.delete_front()
            return 

        new_tail = self.get_nth(self.length - 1)
        self._delete_node(self.tail)

        self.tail = new_tail
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


if __name__ == "__main__":
    ll = LinkedList([1,2,3,4,5,7])
    ll.delete_end()
    ll.delete_front()
    ll.delete_with_key(6)
    ll.insert_sorted(6)
    for node in ll:
        print(node, end="->")
    print()

