import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("How many dice?:"))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# donne les dés verticalement

# for die in range(num_of_dice):              # for every "die" in our range of our number of dice
#    for line in dice_art.get(dice[die]):     # for every line in our dictionary, get our dice at index of our counter "die"
#        print(line)

# donne les dés horizontalement
for line in range(5):                           # on veut print la 1ère ligne de chaque dé, puis la 2ème, etc... (->5)
    for die in dice:                            # pour chaque dé dans la liste
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die

print(dice)
print(f"Total: {total}")
