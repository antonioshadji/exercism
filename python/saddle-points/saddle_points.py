def saddle_points(matrix):
    if not matrix:
        return set()

    length = len(matrix[0])
    cols = dict()
    row_set = set()

    for i, row in enumerate(matrix):
        if len(row) != length:
            raise ValueError('irregular matrix')
        c = row.index(max(row))
        row_set.add((i, c))
        while True:
            try:
                c = row.index(max(row), c + 1)
                row_set.add((i, c))
            except ValueError:
                break
        for j, col in enumerate(row):
            col_min = cols.get(j, (999,))
            value = matrix[i][j]
            if value < col_min[0]:
                cols[j] = (value, (i, j))
            elif value == col_min[0]:
                cols[j] += ((i, j),)

    col_set = set()
    for k in cols:
        for i in range(1, len(cols[k])):
            col_set.add(cols[k][i])

    return row_set & col_set


if __name__ == '__main__':
    m = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]

    print(saddle_points(m))
