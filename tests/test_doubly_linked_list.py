def test_head_equals_tail(empty_doubly_linked_list):
    empty_doubly_linked_list.insert_end(1)
    assert empty_doubly_linked_list.head == empty_doubly_linked_list.tail


def test_head_next_equals_tail(empty_doubly_linked_list):
    empty_doubly_linked_list.insert_end(1)
    empty_doubly_linked_list.insert_end(2)
    assert empty_doubly_linked_list.head.next == empty_doubly_linked_list.tail


def test_insertion(empty_doubly_linked_list):
    empty_doubly_linked_list.insert_end(1)
    assert list(empty_doubly_linked_list) == [1]

    empty_doubly_linked_list.insert_end(2)
    assert list(empty_doubly_linked_list) == [1, 2]

    empty_doubly_linked_list.insert_end(45)
    assert list(empty_doubly_linked_list) == [1, 2, 45]

    empty_doubly_linked_list.insert_front(99)
    assert list(empty_doubly_linked_list) == [99, 1, 2, 45]

    empty_doubly_linked_list.insert_end(11)
    assert list(empty_doubly_linked_list) == [99, 1, 2, 45, 11]

    empty_doubly_linked_list.insert_front(78)
    assert list(empty_doubly_linked_list) == [78, 99, 1, 2, 45, 11]

    empty_doubly_linked_list.insert_sorted(6)
    assert list(empty_doubly_linked_list) == [6, 78, 99, 1, 2, 45, 11]

    empty_doubly_linked_list.insert_sorted(120)
    assert list(empty_doubly_linked_list) == [6, 78, 99, 1, 2, 45, 11, 120]


def test_deletion(filled_doubly_linked_list):
    filled_doubly_linked_list.delete_front()
    assert list(filled_doubly_linked_list) == [78, 99, 1, 2, 45, 11, 120]

    filled_doubly_linked_list.delete_end()
    assert list(filled_doubly_linked_list) == [78, 99, 1, 2, 45, 11]

    filled_doubly_linked_list.delete_with_key(45)
    assert list(filled_doubly_linked_list) == [78, 99, 1, 2, 11]

    filled_doubly_linked_list.delete_front()
    assert list(filled_doubly_linked_list) == [99, 1, 2, 11]

    filled_doubly_linked_list.delete_with_key(99)
    assert list(filled_doubly_linked_list) == [1, 2, 11]

    filled_doubly_linked_list.delete_end()
    assert list(filled_doubly_linked_list) == [1, 2]

    filled_doubly_linked_list.delete_end()
    assert list(filled_doubly_linked_list) == [1]

    filled_doubly_linked_list.delete_front()
    assert list(filled_doubly_linked_list) == []


def test_list_length(filled_doubly_linked_list):
    filled_doubly_linked_list.delete_front()
    assert len(filled_doubly_linked_list) == 7
