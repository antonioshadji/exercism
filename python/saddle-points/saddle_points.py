import numpy as np


def saddle_points(matrix):
    if not matrix:
        return set()

    length = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != length:
            raise ValueError('irregular matrix')

    row_set = set(zip(range(len(matrix[0])), np.argmax(matrix, axis=1)))
    col_set = set(zip(np.argmin(matrix, axis=0), range(len(matrix))))

    return row_set & col_set


if __name__ == '__main__':
    m = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]

    print(saddle_points(m))


# m = [[9, 8, 7],
#      [5, 3, 2],
#      [6, 6, 7]]
# rows {(0, 1), (0, 0), (2, 2)}
# cols {(1, 2), (1, 0), (1, 1)}
