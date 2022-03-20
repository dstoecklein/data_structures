from singly_linked_list import SinglyLinkedList


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # insert
    def enqueue(self, data):
        self.items.append(data)

    # remove
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items.pop(0)

    # return first
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items[0]

    # delete all
    def delete(self):
        self.items = None


q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q)


# allocate only needed memory
class CircularQueue:
    def __init__(self, size):
        self.items = [None] * size
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            return "Queue is full!"
        else:
            if self.top + 1 == self.size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = data

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        first = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first

    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items[self.start]

    def delete(self):
        self.items = self.size * [None]
        self.top = -1
        self.start = -1


print("===")
cq = CircularQueue(3)
print(cq.isFull())
print(cq.isEmpty())
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.dequeue()
print(cq)


class LinkedListQueue:
    def __init__(self):
        self.linkedList = SinglyLinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def isEmpty(self):
        return self.linkedList.isEmpty()

    def enqueue(self, data):
        self.linkedList.insert_sorted(data)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.linkedList.delete_front()

    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


print("===")
llq = LinkedListQueue()
print(llq.isEmpty())
llq.enqueue(1)
llq.enqueue(2)
llq.enqueue(3)
print(llq)
llq.dequeue()
print(llq)
print(llq.peek())
