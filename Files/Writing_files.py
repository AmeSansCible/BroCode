# 📁 MÉMO : Python Writing Files (.txt, .json, .csv)

# 🎯 Modes d'ouverture :
#   "r" = lecture (read), erreur si le fichier n'existe pas
#   "w" = écriture (write), crée ou écrase le fichier
#   "a" = ajout (append), ajoute à la fin du fichier
#   "x" = création exclusive, erreur si le fichier existe déjà

# ✅ FICHIERS .TXT
#   Écriture :
#       with open("fichier.txt", "w") as file:
#           file.write("ligne 1\n")
#           file.write("ligne 2\n")
#
#   Ajout :
#       with open("fichier.txt", "a") as file:
#           file.write("nouvelle ligne\n")
#
#   Lecture :
#       with open("fichier.txt", "r") as file:
#           contenu = file.read()

# ✅ FICHIERS .JSON
#   import json
#
#   Écriture :
#       with open("data.json", "w") as file:
#           json.dump(donnees, file, indent=4)
#
#   Lecture :
#       with open("data.json", "r") as file:
#           data = json.load(file)

# ✅ FICHIERS .CSV
#   import csv
#
#   Écriture :
#       with open("data.csv", "w", newline='') as file:
#           writer = csv.writer(file)
#           for row in list:
#               writer.writerow(row)
#
#   Lecture :
#       with open("data.csv", "r") as file:
#           reader = csv.reader(file)
#           for ligne in reader:
#               print(ligne)


txt_data = "I like pizza!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

# OU
try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

