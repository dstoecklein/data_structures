class Node():
    __slots__ = "data", "idx", "next", "prev"
    def __init__(self, idx, data=None, next=None, prev=None):
        self.data = data
        self.idx = idx
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}@{self.idx}'

class SparseArray():
    def __init__(self, array_length):
        self.head = Node(idx=1, data=None)
        self.tail = Node(idx=1, data=None)
        self.length = 1 # because of dummy node creation
        self.array_length = array_length # if we need an array of length n

    def __len__(self):
        return self.length

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    @staticmethod
    def _link(node1, node2):
        if node1:
            node1.next = node2
        if node2:
            node2.prev = node1

    def _embed_node_after(self, node, idx, data=None):
        new_node = Node(idx=idx, data=data)
        self._link(new_node, node.next)
        self._link(node, new_node)
        self.length += 1
    
    def isempty(self):
        return self.length == 0

    def get_node(self, idx, create_if_not_exist=True):
        curr = self.head
        while curr.next and curr.next.idx < idx: # search for node with idx
            curr = curr.next

        if curr.next and curr.next.idx == idx: # found
            return curr.next
        
        if not create_if_not_exist:
            return None

        # if not found, embed node after curr
        node = self._embed_node_after(node=curr, idx=idx, data=None)
        return node

    def get_value(self, idx):
        assert 0 <= idx # negativ idx not allowed
        assert idx < self.array_length # idx greater than array length doesnt make sense
        node = self.get_node(idx=idx, create_if_not_exist=False)

        if not node:
            return None

        return node.data

    def set_value(self, idx, data):
        # get node, create if doesnt exist, overwrite its data value
        assert 0 <= idx # negativ idx not allowed
        assert idx < self.array_length # idx greater than array length doesnt make sense
        self.get_node(idx=idx, create_if_not_exist=True).data = data

    def add(self, other):
        assert self.array_length == other.array_length
        if not self.array_length:
            return
        
        # Iterate on the other first, add it to the current
        curr = other.head.next
        while curr:
            node = self.get_node(idx=curr.idx, create_if_not_exist=True)
            if node.data is None:
                node.data = curr.data
            else:
                node.data += curr.data
            curr = curr.next

if __name__ == "__main__":
    sa = SparseArray(5)
    sa.get_node(idx=1)
    sa.set_value(idx=1, data=5)
    for item in sa:
        print(item.idx, item.data)
