import pytest

from lists.doubly_linked_list import DoublyLinkedList
from lists.singly_linked_list import SinglyLinkedList
from lists.sparse_matrix import SparseMatrix

@pytest.fixture()
def empty_singly_linked_list():
    empty_singly_linked_list = SinglyLinkedList()
    return empty_singly_linked_list


@pytest.fixture()
def filled_singly_linked_list():
    filled_singly_linked_list = SinglyLinkedList([6, 78, 99, 1, 2, 45, 11, 120])
    return filled_singly_linked_list


@pytest.fixture()
def empty_doubly_linked_list():
    empty_doubly_linked_list = DoublyLinkedList()
    return empty_doubly_linked_list


@pytest.fixture()
def filled_doubly_linked_list():
    filled_doubly_linked_list = DoublyLinkedList([6, 78, 99, 1, 2, 45, 11, 120])
    return filled_doubly_linked_list


@pytest.fixture()
def empty_sparse_matrix1():
    empty_sparse_matrix1 = SparseMatrix(2,2)
    return empty_sparse_matrix1


@pytest.fixture()
def empty_sparse_matrix2():
    empty_sparse_matrix2 = SparseMatrix(2,2)
    return empty_sparse_matrix2