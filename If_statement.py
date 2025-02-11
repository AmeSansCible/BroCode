# if = Do some code only IF some condition is TRUE
#      Else do something else

age = int(input("Enter your age:"))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up.")


response = input("Would you like food (Y/N)? :")
if response == "Y":
    print("Let's order !")
elif response == "N":
    print("I want so let's order anw...")
else:
    print("Too hard to say Y or N ???")


name = input("Enter your name:")

if name == "":
    print("How come you forgot your name dumbass ???")
else:
    print(f"Sweet, I'm sure to never name my kid like this, {name}.")