import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        # Création de 3 boutons (le texte affiché est "#1", "#2", "#3")
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        # Ensuite, on configure tout le visuel avec une méthode à part (bonne habitude)
        self.initUi()

    # fonction qui sert à organiser tout ce qui est User Interface (tout ce qu'on voit à l'écran) : visuel + réaction de l'interface
    def initUi(self):
        # On crée un widget central (obligatoire pour que la fenêtre affiche quelque chose)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # On crée un layout horizontal = les boutons vont être alignés côte à côte
        hbox = QHBoxLayout()

        # On place les 3 boutons dans ce layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # On attache ce layout au widget central pour que ça s'affiche dans la fenêtre
        central_widget.setLayout(hbox)

        # On donne un nom à chaque bouton (important pour les repérer dans le style CSS)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Ici on définit du style CSS comme sur un site web pour personnaliser les boutons :
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;         /* Taille du texte */
                font-family: Arial;      /* Police d’écriture */
                padding: 15px 75px;      /* Espace à l’intérieur du bouton (haut/bas + gauche/droite) */
                margin: 25px;            /* Espace entre les boutons */
                border: 3px solid;       /* Bordure simple */
                border-radius: 15px;     /* Coins arrondis */
            }

            /* Style spécial pour chaque bouton grâce à leur ID (défini avec setObjectName) */
            QPushButton#button1{
                background-color: hsl(4, 54%, 50%);
            }
            QPushButton#button2{
                background-color: hsl(220, 51%, 57%);
            }
            QPushButton#button3{
                background-color: hsl(147, 55%, 56%);
            }

            /* Quand on survole un bouton, sa couleur change (effet hover comme en HTML/CSS) */
            QPushButton#button1:hover{
                background-color: hsl(4, 54%, 70%);
            }
            QPushButton#button2:hover{
                background-color: hsl(220, 51%, 77%);
            }
            QPushButton#button3:hover{
                background-color: hsl(147, 55%, 76%);
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    