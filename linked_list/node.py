class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}'


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)

    node1.next = node2

    print(node1)
    print(node2)

    # check link
    print(id(node2))
    print(id(node1.next))