class vec:
	instance = 0
	def __init__(self, list_elem):
		self.x = list_elem[0]
		self.y = list_elem[1]
		self.z = list_elem[2]
		self.w = list_elem[3]
		vec.instance += 1

	#get
	def get_x():
		return self.x

	def get_y():
		return self.y

	def get_z():
		return self.z
	
	def get_w():
		return self.w

	def get_instance():
		return self.instance

	# set
	def set_x(x):
		self.x = x

	def set_y(y):
		self.y = y

	def set_z(z):
		self.z = z

	def set_w(w):
		self.w = w

# v1 = vec([0.0, 1.0, 2.0, 3.0])
# print(v1)
# print(v1.x, v1.y, v1.z, v1.w)