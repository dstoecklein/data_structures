from traceback import print_last


class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}'

def print_lst(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next
    print()

def print_rec(head):
    if head is not None:
        print(head.data, end='->')
        print_rec(head.next)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    print_lst(node1)
    print_rec(node1)
