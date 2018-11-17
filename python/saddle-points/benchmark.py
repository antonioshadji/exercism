import timeit

setup = 'from saddle_points import saddle_points'
stmt = 'saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])'

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
# 6.256525141012389
