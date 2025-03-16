# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

# Evite la duplication de code, facilite la maintenance et permet d'ajouter des fonctionnalités
# supplémentaires en gardant le comportement de la classe mère

class Shape:                                # superclass
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It's {self.color} and {"filled" if self.filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)         # on appelle le constructeur de Shape, ce qui évite de réécrire le code pour color et filled
        self.radius = radius

    def describe(self):
        print(f"It's a circle with an area of {3.14 * self.radius * self.radius} cm^2")
        super().describe()                      # appelle la méthode de la classe parent


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)         # hérite des attributs de la classe mère
        self.width = width

    def describe(self):
        print(f"It's a square with an area of {self.width * self.width} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It's a triangle with an area of {self.width * self.height / 2} cm^2")
        super().describe()


circle = Circle("red", False, 3)
square = Square("blue", True, 6)
triangle = Triangle("yellow", True, 3, 5)

triangle.describe()
