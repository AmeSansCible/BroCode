import math

# Exercice 1 = calculer la circonférence d'un cercle
radius = float(input("Enter the radius of a circle:"))
circ = 2 * math.pi * radius
print(f"The circumference is {round(circ, 2)}cm.")     # arrondi la réponse à 2 décimales


# Exercice 2 = calculer la surface d'un cercle

radius = float(input("Enter the radius of a circle:"))
area = math.pi * pow(radius, 2)

print(f"The area is {round(area, 2)}cm^2.")     # arrondi la réponse à 2 décimales


# Exercise 3 = calculer l'hypothénuse d'un triangle rectangle

a = float(input("Enter the length of a :"))
b = float(input("Enter the length of b :"))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypothenus is {c}cm.")
