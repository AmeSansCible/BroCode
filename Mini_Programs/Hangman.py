import random

# si on veut créer une plus grande quantité de mots : new python file puis : from nom_du_fichier import words (puis supprimer la liste là en dessous)
words = ("apple", "orange", "banana", "coconut")

#dictionary of key:()    chaque clé correspond au nombre de mauvaises réponses
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "   "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("********")



def display_hint(hint):
    print(" ".join(hint))           # for each character within our hint join it by an empty space

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():      # vérifie que le guess ne soit qu'une seule LETTRE
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:                     # si la lettre guess est dans answer
            for i in range(len(answer)):        # parcourt chaque indice i du mot answer, de 0 jusqu'à la longueur du mot moins 1.
                if answer[i] == guess:          # compare la lettre de answer à la position i avec guess
                    hint[i] = guess             # remplace _ par guess
        else:
            wrong_guesses += 1


        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()