ma_liste = ['a','b','c','d','e','f','g','h']
for index, elem in enumerate(ma_liste):
	# tres idiot les arguments sont inversés ds leurs utilisations
	print("to index {} find the element {}.".format(index, elem))
for elem in enumerate(ma_liste):
	print(elem)