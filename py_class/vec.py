import numbers
# import decimal
# >>> [isinstance(x, numbers.Number) for x in (0, 0.0, 0j, decimal.Decimal(0))]
# [True, True, True, True]

class vec:
	instance = 0
	#ssize = 0
	value = []
	# NumberTypes = (types.IntType, types.LongType, types.FloatType, types.ComplexType)
	def __init__(self, elem):
		if isinstance(elem, list):
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

	# add	
	def add(self, elem):
		index = 0
		res = []
		if isinstance(elem, vec) and self.size == elem.size:
			while (index < self.size):
				res.append(self.value[index] + elem.value[index])
				index += 1
		elif isinstance(elem, numbers.Number):
			while (index < self.size):
				res.append(self.value[index] + elem)
				index += 1
		return vec(res)

	# add dunder method or magic method
	def __add__(self, elem):
		return self.add(elem)
	
	def __radd__(self, elem):
		return self.add(elem)


	# sub	
	def sub(self, elem):
		index = 0
		res = []
		if isinstance(elem, vec) and self.size == elem.size:
			while (index < self.size):
				res.append(self.value[index] - elem.value[index])
				index += 1
		elif isinstance(elem, numbers.Number):
			while (index < self.size):
				res.append(self.value[index] - elem)
				index += 1
		return vec(res)

	# sub dunder method or magic method
	def __sub__(self, elem):
		return self.sub(elem)
	
	def __rsub__(self, elem):
		return self.sub(elem)

	

	# mul	
	def mul(self, elem):
		index = 0
		res = []
		if isinstance(elem, vec) and self.size == elem.size:
			while (index < self.size):
				res.append(self.value[index] * elem.value[index])
				index += 1
		elif isinstance(elem, numbers.Number):
			while (index < self.size):
				res.append(self.value[index] * elem)
				index += 1
		return vec(res)

	# mul dunder method or magic method
	def __mul__(self, elem):
		return self.mul(elem)
	
	def __rmul__(self, elem):
		return self.mul(elem)


	# truediv	
	def truediv(self, elem):
		index = 0
		res = []
		if isinstance(elem, vec) and self.size == elem.size:
			while (index < self.size):
				res.append(self.value[index] / elem.value[index])
				index += 1
		elif isinstance(elem, numbers.Number):
			while (index < self.size):
				res.append(self.value[index] / elem)
				index += 1
		return vec(res)

	# truediv dunder method or magic method
	def __truediv__(self, elem):
		return self.truediv(elem)
	
	def __rtruediv__(self, elem):
		return self.truediv(elem)
	
	
	# floordiv	
	def floordiv(self, elem):
		index = 0
		res = []
		if isinstance(elem, vec) and self.size == elem.size:
			while (index < self.size):
				res.append(self.value[index] // elem.value[index])
				index += 1
		elif isinstance(elem, numbers.Number):
			while (index < self.size):
				res.append(self.value[index] // elem)
				index += 1
		return vec(res)


	# floordiv dunder method or magic method
	def __floordiv__(self, elem):
		return self.floordiv(elem)
	
	def __rfloordiv__(self, elem):
		return self.floordiv(elem)



	# print class
	def __repr__(self):
		return "(vec " +str(self.value) + ")"

	def __str__(self):
		return "(vec " +str(self.value) + ")"

	def dot(self, other):
		res = 0
		index = 0
		while (index < self.size):
			res += (self.value[index] * other.value[index])
			index += 1
		return res

