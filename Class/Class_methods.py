# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0                               # variables de classe (partagées par tous les étudiants)
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name                    # attributs propres à chaque élève
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD (agit sur un seul étudiant)
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod                                          # affecte toute la classe (donc tous les étudiants)
    def get_count(cls):                                   # Elle peut fonctionner sans créer d'instance
        return f"Total number of students: {cls.count}"   # (ne dépend pas d'un étudiant en particulier mais de la classe entière)
                                                          # Même sans étudiants créés, elle peut être appelée

    @classmethod                                          # Elle accède aux variables de classe
    def get_average_gpa(cls):                             # On peut calculer la moyenne des GPA sans créer une instance.
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Spongebob", 3.2)
student1 = Student("Patrick", 2.0)
student1 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())