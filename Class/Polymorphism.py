# Polymorphism = Greek word that means to "have many forms or faces"

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

# ABC = signifie Abstract Base Class (Classe de base abstraite).
# abstractmethod : permet de marquer une méthode comme obligatoire.
# Cela garantit une structure commune, utile pour la programmation modulaire et évolutive.

class Shape(ABC):           # Shape est une classe abstraite, car elle hérite de ABC
                            # elle ne peut pas être instanciée directement

    @abstractmethod         # indique de area() est une méthode abstraite
                            # toute classe qui hérite de Shape doit obliatoirement la définir
    def area(self):
        pass                # La méthode est définie mais pas implémentée

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]

for shape in shapes:                    # Boucle polymorphique : on appelle la méthode area() sur chaque objet
    print(f"{shape.area()}cm²")