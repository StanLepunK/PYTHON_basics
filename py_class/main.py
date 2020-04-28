from vec import *
v1 = vec([0.0, 0.0, 0.0, 0.0])

print(v1)
#v1.x = 12.0
print("v1:", v1.x, v1.y, v1.z, v1.w)
print("v1.size:", v1.size)
print("v1.value:", v1.value)
v2 = v1 + 2.0
print("v2 + 2.0 =", v2.x, v2.y, v2.z, v2.w)
v3 = v2 * 2.0
print("v3 * 2.0 =", v3.x, v3.y, v3.z, v3.w)
v4 = v3 - 1.5
print("v4 - 1.5 =", v4.x, v4.y, v4.z, v4.w)
v5 = v4 / 0.75
print("v5 / 0.75 =", v5.x, v5.y, v5.z, v5.w)
v6 = v5 // 2
print("v6 // 2 =", v6.x, v6.y, v6.z, v6.w)

v7 = vec(3)
print("v7.value", v7.value)