from vec import *
v1 = vec([0.0, 2.0, 3.0, 4.0])

print(v1)
#v1.x = 12.0
print("v1:", v1)
print("v1.size:", v1.size)
print("v1.value:", v1.value)

# call __add__
v2 = v1 + 2.0
print("use __add__ v2 + 2.0 =", v2)
# call __radd__
v2 = 2.0 + v1
print("use __radd__ 2.0 + v2 =", v2)


# call __sub__
v2 = v1 - 2.0
print("use __sub__ v2 - 2.0 =", v2)
# call __rsub__
v2 = 2.0 - v1
print("use __rsub__ 2.0 - v2 =", v2)

# v3 = v2 + v1
# print("v2 + v1 = v3", v2, "+", v1, "=", v3)



# v3 = v2 * 2.0
# print("v3 * 2.0 =", v3.x, v3.y, v3.z, v3.w)
# v4 = v3 - 1.5
# print("v4 - 1.5 =", v4.x, v4.y, v4.z, v4.w)
# v5 = v4 / 0.75
# print("v5 / 0.75 =", v5.x, v5.y, v5.z, v5.w)
# v6 = v5 // 2
# print("v6 // 2 =", v6.x, v6.y, v6.z, v6.w)

# v7 = vec(3)
# print("v7.value", v7.value)

# print("v1.dot(v2):", v1.dot(v2))