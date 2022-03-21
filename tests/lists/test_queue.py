def test_python_list_queue_is_empty(empty_python_list_queue):
    assert empty_python_list_queue.isEmpty() is True


def test_circular_queue_is_empty(empty_circular_queue):
    assert empty_circular_queue.isEmpty() is True
    assert empty_circular_queue.isFull() is False


def test_circular_queue_is_full(full_circular_queue):
    assert full_circular_queue.isEmpty() is False
    assert full_circular_queue.isFull() is True


def test_python_list_queue_function(empty_python_list_queue):
    empty_python_list_queue.enqueue(1)
    empty_python_list_queue.enqueue(2)
    assert str(empty_python_list_queue) == "1 2"

    empty_python_list_queue.enqueue(1)
    empty_python_list_queue.enqueue(2)
    empty_python_list_queue.enqueue(3)
    empty_python_list_queue.enqueue(0)
    empty_python_list_queue.enqueue(256)
    empty_python_list_queue.enqueue(27891)
    empty_python_list_queue.enqueue(21234654789798)
    assert str(empty_python_list_queue) == "1 2 1 2 3 0 256 27891 21234654789798"
    assert str(empty_python_list_queue.peek()) == "1"

    empty_python_list_queue.enqueue("test")
    assert str(empty_python_list_queue) == "1 2 1 2 3 0 256 27891 21234654789798 test"

    empty_python_list_queue.dequeue()
    assert str(empty_python_list_queue) == "2 1 2 3 0 256 27891 21234654789798 test"
    assert str(empty_python_list_queue.peek()) == "2"

    assert empty_python_list_queue.delete() is None


def test_circular_queue_function(empty_circular_queue):
    # init with size 10
    empty_circular_queue.enqueue(1)
    empty_circular_queue.enqueue(2)
    assert str(empty_circular_queue) == "1 2 None None None None None None None None"

    empty_circular_queue.enqueue(1)
    empty_circular_queue.enqueue(2)
    empty_circular_queue.enqueue(3)
    empty_circular_queue.enqueue(0)
    empty_circular_queue.enqueue(256)
    empty_circular_queue.enqueue(27891)
    empty_circular_queue.enqueue(21234654789798)
    assert str(empty_circular_queue) == "1 2 1 2 3 0 256 27891 21234654789798 None"
    assert str(empty_circular_queue.peek()) == "1"

    empty_circular_queue.enqueue("test")
    assert str(empty_circular_queue) == "1 2 1 2 3 0 256 27891 21234654789798 test"

    empty_circular_queue.dequeue()
    assert str(empty_circular_queue) == "None 2 1 2 3 0 256 27891 21234654789798 test"
    assert str(empty_circular_queue.peek()) == "2"

    assert empty_circular_queue.delete() is None

    assert empty_circular_queue.dequeue() == "Queue is empty!"
    assert empty_circular_queue.peek() == "Queue is empty!"


def test_linked_list_queue_function(empty_linked_list_queue):
    # init with size 10
    empty_linked_list_queue.enqueue(1)
    empty_linked_list_queue.enqueue(2)
    assert str(empty_linked_list_queue) == "1 2"

    empty_linked_list_queue.enqueue(1)
    empty_linked_list_queue.enqueue(2)
    empty_linked_list_queue.enqueue(3)
    empty_linked_list_queue.enqueue(0)
    empty_linked_list_queue.enqueue(256)
    empty_linked_list_queue.enqueue(27891)
    empty_linked_list_queue.enqueue(21234654789798)
    assert str(empty_linked_list_queue) == "1 2 1 2 3 0 256 27891 21234654789798"
    assert str(empty_linked_list_queue.peek()) == "1"

    empty_linked_list_queue.enqueue("test")
    assert str(empty_linked_list_queue) == "1 2 1 2 3 0 256 27891 21234654789798 test"

    empty_linked_list_queue.dequeue()
    assert str(empty_linked_list_queue) == "2 1 2 3 0 256 27891 21234654789798 test"
    assert str(empty_linked_list_queue.peek()) == "2"

    assert empty_linked_list_queue.delete() is None

    assert empty_linked_list_queue.dequeue() == "Queue is empty!"
    assert empty_linked_list_queue.peek() == "Queue is empty!"
