def test_sparse_matrix_addition(empty_sparse_matrix1, empty_sparse_matrix2):
    mat1 = empty_sparse_matrix1
    mat2 = empty_sparse_matrix2

    mat1.set_value(0, 0, 1)
    mat1.set_value(0, 1, 2)
    mat1.set_value(1, 0, 3)
    mat1.set_value(1, 1, 4)

    mat2.set_value(0, 0, 2)
    mat2.set_value(0, 1, 4)
    mat2.set_value(1, 0, 1)
    mat2.set_value(1, 1, 3)


    mat2.add(mat1)

    result = str(mat2)
    expected = "Row 0: idx:0 data:3, idx:1 data:6, \nRow 1: idx:0 data:4, idx:1 data:7, "

    assert result == expected