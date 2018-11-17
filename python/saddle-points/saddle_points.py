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
        if row.count(max(row)) > 1:
            while True:
                try:
                    c = row.index(max(row), c + 1)
                    row_set.add((i, c))
                except ValueError:
                    break
        for j, col in enumerate(row):
            col_min = cols.get(j, (999,))
            if col < col_min[0]:
                cols[j] = (col, (i, j))
            elif col == col_min[0]:
                cols[j] += ((i, j),)

    col_set = set()
    for k in cols:
        if len(cols[k]) > 2:
            for i in range(1, len(cols[k])):
                col_set.add(cols[k][i])
        else:
            col_set.add(cols[k][1])

    return row_set & col_set


if __name__ == '__main__':
    m = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]

    print(saddle_points(m))
