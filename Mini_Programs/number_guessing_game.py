import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess:")
    if guess.isdigit():                     # si le guess est uniquement en chiffres
        guess = int(guess)                  # transforme la string en integer
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, try again.")
        elif guess > answer:
            print("Too high, try again.")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False                 # Sort de la boucle lorsque la réponse est trouvée
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
