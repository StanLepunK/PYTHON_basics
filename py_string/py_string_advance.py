arg = 3.123456789
# absence de sépateur est considéré comme un espace séparateur
string = str(arg)
print(string.split())
gauche, droite = string.split(".")
print(gauche,droite)
print(",".join([gauche, droite[:3]]))
#print(arg.split("e"))