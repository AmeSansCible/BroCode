# class variables =  Shared among all instances of a class
#                    Defined outside the constructor
#                    Allow you to share data among all objects created from that class

class Student:

    class_year = 2024               # variable partagée par tous les objets d'une même classe
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1   # si on modifie une class variable on utilise le nom de la classe plutôt que self

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)


print(Student.class_year)           # pour accéder à une class variable on appelle le nom de la classe et la variable (pour + de lisibilité)
print(student1.class_year)          # mais c'est également posssible d'y accéder depuis un objet

print(f"My graduating class of {Student.class_year} has {Student.num_students} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
