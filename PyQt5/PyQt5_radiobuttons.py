import sys
import jurigged
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)

        # Création de deux groupes de boutons : ils permettent de lier certains boutons ensemble
        # (ex. un seul bouton sélectionnable par groupe)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)


        self.initUi()


    def initUi(self):
        # Positionne les boutons radio dans la fenêtre (x, y, largeur, hauteur)
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # Change le style de tous les boutons radio (police, taille, padding…)
        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        # Ajoute les boutons radio à leurs groupes respectifs
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connecte chaque bouton radio à une fonction (quand il est activé/désactivé)
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


    # Fonction appelée quand un bouton radio est activé
    def radio_button_changed(self):
        radio_button = self.sender()                     # "sender" = bouton qui a déclenché l’événement
        if radio_button.isChecked():                     # On vérifie s’il est coché
            print(f"{radio_button.text()} is selected")  # On affiche le texte du bouton



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()