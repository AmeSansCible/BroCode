# Static methods = A method that belongs to a class rather tan any object form that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

# Quand l'utiliser : Quand la méthode ne dépend ni de l'instance (self) ni de la classe
#                    Quand on veut une fonction utilitaire qui appartient à une classe mais qui pourrait être une fonction normale
#                    Exemples : fonctions mathématiques, outils, validation de données

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):                                # méthode appartenant à une classe
                                                                    # mais qui ne nécessitent pas d'instance (self) pour être appelée
        valid_positions = ["Manager", "Cashier", "Cook", "Janito"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Cook"))                   # Classe.méthode
print(employee1.get_info())                                 # objet.méthode
print(employee2.get_info())
print(employee3.get_info())