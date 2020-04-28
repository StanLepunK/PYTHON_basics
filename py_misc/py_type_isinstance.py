#import numbers
a = input("C'est quoi ton type, moi c'est les nombre entier ? ")
print(type(a))
if isinstance(a, int):
#if isinstance(a, numbers.Integral):
	print("toi t'es un mec entier")
elif isinstance(a, float):
	print("toi t'es un petit float")
else:
	print("en faite t'es peut-être un vieux string, parce input y cast que dalle")