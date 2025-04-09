# 📖 MÉMO : Python Reading Files (.txt, .json, .csv)

# 🎯 Modes d'ouverture :
#   "r" = lecture (read) → défaut si non précisé
#   Toujours utiliser : with open(...) as file → fermeture automatique

# ✅ FICHIERS .TXT
#   Lire tout :
#       with open("fichier.txt", "r") as file:
#           contenu = file.read()
#           print(contenu)
#
#   Lire ligne par ligne :
#       with open("fichier.txt", "r") as file:
#           for ligne in file:
#               print(ligne.strip())

# ✅ FICHIERS .JSON
#   import json
#
#   Lecture :
#       with open("data.json", "r") as file:
#           data = json.load(file)
#           print(data["clé"])  # accéder à une valeur

# ✅ FICHIERS .CSV
#   import csv
#
#   Lecture :
#       with open("data.csv", "r") as file:
#           reader = csv.reader(file)
#           for ligne in reader:
#               print(ligne)
#
#   Lecture avec dictionnaires (en-têtes → clés) :
#       with open("data.csv", "r") as file:
#           reader = csv.DictReader(file)
#           for ligne in reader:
#               print(ligne["Nom"])

