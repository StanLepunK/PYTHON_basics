def mult(x, y):
	return x * y

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def div(x, y):
	return x / y

def mod(x, y):
	return x % y


if __name__ == "__main__":
	print("add x = 1, y = 1", add(1,1))
	print("sub x = 2, y = 1", sub(2,1))
	print("mult x = 2, y = 2", mult(2,2))
	print("div x = 10, y = 2", div(10,2))
	print("mod x = 11, y = 2", mod(11,2))
