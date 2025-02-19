import random

options = ("rock", "paper", "scissors")
running = True

while running :                                 # On met tout dans une boucle pour pouvoir continuer à jouer

    player = None                               # à chaque début de partie on reset le player et le computer
    computer = random.choice(options)

    while player not in options:                    # while our player variable is not found in our options, the while loop continue forever
        player = input("Enter a choice (rock, paper, scissors):").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Do you want to keep playing (y/n)?:").lower() == "y":
        running = False

print("Thanks for playing!")