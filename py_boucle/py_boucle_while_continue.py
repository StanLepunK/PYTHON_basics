x = 1
while x < 20: # Tant que i est inférieure à 20
    if x % 3 == 0:
        x += 4 # On ajoute 4 à i
        print("On incrémente x de 4")
        if x == 7:
        	continue # On retourne au while sans exécuter les autres lignes
        print("x n'était pas égale à 7 mais à",x,"c'est pour ça qu'on est là\n")
    print("La variable x =", x)
    x += 1 # Dans le cas classique on ajoute juste 1 à x
print("\nallez aurevoir", x)