# dictionary = a collection of {key: value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("USA")) # donne la valeur de la clé

# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})  # ajoute ou modifie une key:value pair
# capitals.pop("China")                   # supprime une key:value pair
# capitals.popitem()                      # supprime la dernière key:value pair
# capitals.clear()                        # supprime tout ce qu'il y a dans le dictionnaire

# keys = capitals.keys()                  # donne toutes les clés du dictionnaire

# for key in capitals:
#     print(key, end=" ")

# values = capitals.values()              # donne toutes les valeurs du dictionnaire

# for value in capitals.values():
#     print(value, end=" ")

items = capitals.items()                  # donne une 2D list de tuples

for key, value in capitals.items():
    print(f"{key}: {value}")