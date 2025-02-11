# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
# C'est utile quand l'utilisateur met ses propres valeurs (STR) et qu'on veut les convertir en nombre (INT) par ex

name = "Bro code"
age = 27
gpa = 3.2
is_student = False

# Exemples
age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

# input() = a function that prompts the user to enter data. Returns the entered data as a string

name = input("What is your name ?:")

# pour changer la str en int
age = int(input("How old are you ?:"))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old.")
