# collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple   = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ("apple", "orange", "banana", "coconut")
# fruits = {"apple", "orange", "banana", "coconut"}
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))   # liste toutes les méthodes liées à la collection
# print(help(fruits))  # donne toutes les fonctionnalités de la collection
# print(len(fruits))   # donne la longueur de la collection
# print("pineapple" in fruits)  # vérifie si la string se trouve dans la collection
# for fruit in fruits:
#     print(fruit)



# fruits[0] = "pineapple"   # on peut changer un élément dans la liste
# fruits.append("pineapple")  # on peut ajouer un élément dans une liste
# fruits.remove("apple")      # on peut supprimer un élément dans une liste OU un set
# fruits.insert(0, "pineapple")    # on peut ajouter un élément à l'index qu'on veut
# fruits.sort()  # classe dans l'ordre alphabétique
# fruits.reverse() # ionverse l'ordre
# fruits.clear()   # enlever tous les éléments d'une collection
# fruits.index("apple") # donne l'indexe

