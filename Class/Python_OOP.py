# PYTHON ORIENTED OBJECTS PROGRAMMING
# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# FR : Une classe est un plan de construction
#      Un objet est un exemplaire construit à partir de ce plan
#      Les attributs sont les caractéristiques d'un objet
#      Les méthodes sont les actions qu'un objet peut faire

# les classes prennent généralement beaucoup de place, il est recommandé de créer un nouveau fichier python pour elles
# from le_nom_du_module import Car
class Car:
    def __init__(self, model, year, color, for_sale):     # C'est le constructeur : il permet de donner des caractéristiques aux objets créés.
        self.model = model                                # attribut "model" -> Chaque voiture a un modèle unique
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False)   # on crée des objets avec leurs propres caractéristiques
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

car1.drive()                                                         # chaque objet peut utiliser ses méthodes
car1.stop()
car1.describe()
