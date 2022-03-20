class Node():
    def __init__(self, idx, data=None, next=None, prev=None):
        self.idx = idx
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f'idx:{self.idx} data:{self.data}'

class SparseArray():
    def __init__(self, array_length):
        self.tail = Node(idx=-1)
        self.head = Node(idx=-1)
        self.length = 0 
        self.array_length = array_length

    def __repr__(self):
        string = ''
        curr = self.head.next

        while curr is not None:
            string += str(curr) + ', '
            curr = curr.next

        return string

    def __iter__(self):
        curr = self.head.next
        for i in range(self.array_length):
            if curr and curr.idx == i:
                yield curr.data
                curr = curr.next

    @staticmethod
    def _link(node1, node2):
        if node1:
            node1.next = node2
        if node2:
            node2.prev = node1

    def _embed_after(self, node, idx, data=None):
        new_node = Node(idx=idx, data=data)
        self.length += 1
        self._link(node1=new_node, node2=node.next)
        self._link(node1=node, node2=new_node)
        return new_node

    def _get_node(self, idx, create_if_missing=True):
        curr = self.head

        # iterate over list, start with next cause of dummy node
        while curr.next and curr.next.idx < idx:
            curr = curr.next

        # found it
        if curr.next and curr.next.idx == idx:
            return curr.next

        if not create_if_missing:
            return None

        # create it
        new_node = self._embed_after(node=curr, idx=idx)
        return new_node

    def _print_as_array(self):
        curr = self.head.next
        for i in range(self.array_length):
            if curr and curr.idx == i:
                print(curr.data, end=" ")
                curr = curr.next
            else:
                print(0, end=" ")
        print()

    def set_value(self, idx, data):
        assert 0 <= idx 
        assert idx < self.array_length
        node = self._get_node(idx=idx, create_if_missing=True)
        node.data = data

    def get_value(self, idx):
        assert 0 <= idx
        assert idx < self.array_length
        node = self._get_node(idx=idx, create_if_missing=False)
        if not node:
            return None
        return node.data

    def add(self, other):
        assert self.array_length == other.array_length

        if not self.array_length:
            return

        curr = other.head.next
        while curr:
            node = self._get_node(idx=curr.idx, create_if_missing=True)
            if node.data is None:
                node.data = curr.data
            else:
                node.data += curr.data
            curr = curr.next

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows_sparse_array = SparseArray(array_length=rows)
        self.rows = rows
        self.cols = cols

    def __repr__(self):
        string = ''
        row_node = self.rows_sparse_array.head.next

        while row_node is not None:
            if string != '':
                string += '\n'
            string += f'Row {row_node.idx}: '
            string += str(row_node.data)
            row_node = row_node.next
        return string

    def _print_as_2darray(self, end='\n'):
        row_node = self.rows_sparse_array.head.next

        empty_row = ' '.join(['0'] * self.cols)

        for r in range(self.rows):
            if row_node and row_node.idx == r:
                row_node.data._print_as_array()
                row_node = row_node.next
            else:
                print(empty_row)

        print("")

    def set_value(self, row, col, data):
        assert 0 <= row
        assert row < self.rows
        assert 0 <= col
        assert col < self.cols

        # get target row
        row_node = self.rows_sparse_array._get_node(idx=row, create_if_missing=True)
        # if row not exist, create it with None
        if row_node.data is None:
            row_node.data = SparseArray(array_length=self.cols)

        col_node = row_node.data._get_node(idx=col, create_if_missing=True)
        col_node.data = data

    def get_value(self, row, col):
        assert 0 <= row
        assert row < self.rows
        assert 0 <= col
        assert col < self.cols

        row_node = self.rows_sparse_array._get_node(idx=row, create_if_missing=False)
        if not row_node:
            return None

        col_node = self.rows_sparse_array._get_node(idx=col, create_if_missing=False)
        if not col_node:
            return None

        return col_node.data

    def add(self, other):
        assert self.rows == other.rows and self.cols == other.cols

        # Iterate row by row. Find corresponding row. Add together
        other_row_node = other.rows_sparse_array.head.next
        while other_row_node:
            self_row_node = self.rows_sparse_array._get_node(
                idx=other_row_node.idx, 
                create_if_missing=True
                )

            if self_row_node.data is None:
                self_row_node.data = SparseArray(array_length=self.cols)

            self_row_node.data.add(other=other_row_node.data)
            other_row_node = other_row_node.next

if __name__ == "__main__":
    mat1 = SparseMatrix(2,2)
    mat1.set_value(0, 0, 1)
    mat1.set_value(0, 1, 2)
    mat1.set_value(1, 0, 3)
    mat1.set_value(1, 1, 4)
    mat1._print_as_2darray()

    mat2 = SparseMatrix(2,2)
    mat2.set_value(0, 0, 2)
    mat2.set_value(0, 1, 4)
    mat2.set_value(1, 0, 1)
    mat2.set_value(1, 1, 3)
    mat2._print_as_2darray()

    mat2.add(mat1)
    print(mat2)
    mat2._print_as_2darray()
