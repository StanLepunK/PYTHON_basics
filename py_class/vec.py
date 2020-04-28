class vec:
	instance = 0
	#ssize = 0
	value = []
	def __init__(self, elem):
		if isinstance(elem, list):
			self.x = elem[0]
			self.y = elem[1]
			self.z = elem[2]
			self.w = elem[3]
			self.value = elem
			self.size = len(elem)
		else:
			index = 0;
			# value;
			while index < elem:
				# self.value[index] = index
				self.value.append(index)
				index += 1
		vec.instance += 1

# >>> isinstance([0, 10, 20, 30], list)
# True
# >>> isinstance(50, list)
# False

	# add
	def __add__(self, other):
		res = [self.x + other, self.y + other, self.z + other, self.w + other]
		return vec(res)
	
	def __radd__(self, other):
		res = [self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w]
		return vec(res)

	# dub
	def __sub__(self, other):
		res = [self.x - other, self.y - other,self.z - other,self.w - other]
		return vec(res)

	def __rsub__(self, other):
		res = [self.x - other, self.y - other,self.z - other,self.w - other]
		return vec(res)

	# mult
	def __mul__(self, other):
		res = [self.x * other, self.y * other,self.z * other,self.w * other]
		return vec(res)

	def __rmul__(self, other):
		res = [self.x * other, self.y * other,self.z * other,self.w * other]
		return vec(res)

	# true div
	def __truediv__(self, other):
		res = [self.x / other, self.y / other,self.z / other,self.w / other]
		return vec(res)

	def __rtruediv__(self, other):
		res = [self.x / other, self.y / other,self.z / other,self.w / other]
		return vec(res)
	
	# floor div
	def __floordiv__(self, other):
		res = [self.x // other, self.y // other,self.z // other,self.w // other]
		return vec(res)

	def __rfloordiv__(self, other):
		res = [self.x // other, self.y // other,self.z // other,self.w // other]
		return vec(res)
