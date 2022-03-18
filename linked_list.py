class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class LinkedList():
    def __init__(self, init_data):
        self.head = None
        self.tail = None
        self.length = 0
        self.nodes = []

        if init_data:
            for data in init_data:
                self.insert_end(data)

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def _add_node(self, node):
        self.nodes.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.length -= 1
        else:
            raise RuntimeError("Node not in list!")

    def _delete_next_node(self, node):
        to_delete = node.next
        is_tail = to_delete == self.tail
        node.next = node.next.next
        self._delete_node(to_delete)
        if is_tail:
            self.tail = node

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

    def delete_data(self, data):
        if not self.length:
            return

        if self.head.data == data:
            self.delete_front()
        else:
            temp_prev = None
            temp_curr = self.head
            
            while temp_curr is not None:
                if temp_curr.data == data:
                    self._delete_next_node(temp_prev)
                    break
                temp_prev = temp_curr
                temp_curr = temp_curr.next

    def delete_front(self):
        temp_next = self.head.next
        self._delete_node(temp_next)

        self.head = temp_next
        if self.length <= 1:
            self.tail = self.head

    def get_nth(self, n):
        temp_head = self.head
        counter = 1
        while temp_head is not None:
            if counter == n:
                return temp_head.data
            temp_head = temp_head.next
            counter += 1

    def get_nth_back(self, n):
        if self.length < n:
            return None
        return self.get_nth(self.length - n + 1)

    def swap_pairs(self):
        temp_head = self.head
        while temp_head is not None and temp_head.next is not None:
            temp_head.data, temp_head.next.data = temp_head.next.data, temp_head.data
            temp_head = temp_head.next.next
        
if __name__ == "__main__":
    ll = LinkedList([1,2,3,4,5])
    ll.insert_end(6)

    ll.insert_front(7)
    ll.delete_data(3)
    ll.swap_pairs()
    for node in ll:
        print(node, end="->")
    print()
    print(ll.get_nth_back(2))