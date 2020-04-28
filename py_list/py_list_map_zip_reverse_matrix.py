mat = [[1, 2, 3, 4, 5], [1, 6, 7, 8, 9], [1, 10, 11, 12, 13]]
print("mat",mat)
# mat [[1, 2, 3, 4, 5], [1, 6, 7, 8, 9], [1, 10, 11, 12, 13]]
mat_1 = map(list, zip(*mat))
print("mat 1",mat_1)
# mat 1 <map object at 0x10401ecd0>
mat_2 = list(mat_1)
print("mat 2",mat_2)
# mat 2 [[1, 1, 1], [2, 6, 10], [3, 7, 11], [4, 8, 12], [5, 9, 13]]