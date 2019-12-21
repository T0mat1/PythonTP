def det(matrix, x=1):
    assert (matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]) or matrix.size == 1, "La variable passée en " \
                                                                                          "paramètre doit être une " \
                                                                                          "matrice carrée. "
    if matrix.size == 1:
        return matrix[0]
    for i in matrix.shape[0]:
        pass

