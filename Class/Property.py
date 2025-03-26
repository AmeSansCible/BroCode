# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit : Add additional logic when read, write, or delete attributes
#             Gives you a better, setter and deleter method
#             Utile pour : lire (getter), écrire (setter), supprimer (deleter) un attribut avec contrôle


class Rectangle:
    def __init__(self, width, height):
        # On stocke les vraies valeurs dans des attributs "protégés" (_width, _height)
        self._width = width
        self._height = height

    @property                                           # getter
    def width(self):
        # Permet d'accéder à .width comme un attribut
        return f"{self._width:.1f}cm"

    @property                                           # getter
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter                                       # setter
    def width(self, new_width):
        # Permet d'écrire rectangle.width = X tout en contrôlant la valeur
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter                                      # setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter                                      # deleter
    # Appelé quand on fait "del rectangle.width"
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter                                     # deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

# On modifie les dimensions (appelle les SETTERS)
rectangle.width = 5
rectangle.height = 6

# On supprime les attributs (appelle les DELETERS)
del rectangle.width
del rectangle.height

# On tente d'afficher (appelle les GETTERS)
print(rectangle.width)
print(rectangle.height)
