class Vec3:
	instance = 0
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = x
		Vec3.instance += 1

	def get_x():
		return self.x

	def set_x(x):
		self.x = x

vec_a = Vec3(1.0, 2.0, 3.0)
vec_a.x = 1
print(vec_a.x,vec_a.y,vec_a.z,"num Vec3 instantiate", vec_a.instance)
# vec_b = Vec3()
# vec_b.x = 1
# print(vec_b.x,vec_b.y,vec_b.z,"num Vec3 instantiate",vec_b.instance)
	
