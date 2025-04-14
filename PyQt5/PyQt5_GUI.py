# sys est un module de base de Python qui permet de parler avec le système d’exploitation
# Ici, on l’utilise pour pouvoir quitter l’application proprement à la fin
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


# Ici, je crée ma propre classe "MainWindow", qui représente la fenêtre principale de l’appli
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()                                      # Super important → ça initialise la vraie fenêtre derrière le rideau
        self.setWindowTitle("My cool first GUI")                # Définir les propriétés de la fenêtre (titre et icône)
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        # Ensuite, on configure tout le visuel avec une méthode à part (bonne habitude)
        self.initUi()

    def initUi(self):
        pass


# C’est la porte d’entrée de notre application (comme le bouton ON)
def main():
    app = QApplication(sys.argv)  # On démarre l’application Qt (obligatoire)
    window = MainWindow()         # On crée notre fenêtre personnalisée
    window.show()                 # On affiche la fenêtre
    sys.exit(app.exec_())         # On lance la boucle d’événements, et on quitte proprement à la fin


# Ce truc-là signifie : “si on lance ce fichier directement, on appelle main()”
# (et pas si c’est un import dans un autre fichier)
if __name__ == "__main__":
    main()