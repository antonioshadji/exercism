import timeit


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m[0]))] for i in range(len(m))]


setup = 'from saddle_points import saddle_points'
stmt = 'saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'
# setup = 'from __main__ import transpose_matrix'
# stmt = 'transpose_matrix([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'
# 2.2415304140304215
# 2.1866271650069393

print(timeit.timeit(stmt=stmt, setup=setup, number=1000000))


# algorithm 2
# 12.690007690980565
# after separating cmd, setup
# 11.158029143000022
# 11.076444714970421
# added test if loop needed
# 7.979817851970438
# 7.975111273990478
# added 2nd test if loop needed
# 7.020087717974093
