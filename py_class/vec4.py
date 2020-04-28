class vec4:
	num = 0
	def __init__(self, x, y , z, w):
		self.x = x
		self.y = y
		self.z = x
		self.w = w
		Vec3.num += 1

	#get
	def get_x():
		return self.x

	def get_y():
		return self.y

	def get_z():
		return self.z
	
	def get_w():
		return self.w

	# set
	def set_x(x):
		self.x = x

	def set_y(y):
		self.y = y

	def set_z(z):
		self.z = z

	def set_w(w):
		self.w = w
