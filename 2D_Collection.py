# 2D lists are just a list made up of lists, like ane excel spread sheet

fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =         ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])  # donne l'index 0 de la liste indexée 0


# on peut faire la même chose sans nommer les listes :

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

for collection in groceries:
    print(collection)           # donne chaque liste

for collection in groceries:
    for food in collection:
        print(food, end=" ")             # donne chaque élément de chaque liste, en ligne, séparés par un espace
    print()                              # ajoute une ligne après chaque liste