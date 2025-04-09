import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


# Création de la fenêtre principale
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")                # titre de la fenêtre
        self.setGeometry(700, 300, 500, 500)                    # position et taille de la fenêtre (x, y, largeur, hauteur)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))    # icone de la fenêtre

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: #292929;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom) #VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter) #VERTICALLY CENTER

        #label.setAlignment(Qt.AlignRight) #HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignHCenter) #HORIZONTALLY CENTER
        #label.setAlignment(Qt.alignLeft) #HORIZONTALLY LEFT

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #CENTER & TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #CENTER & BOTTOM
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #CENTER & CENTER
        label.setAlignment(Qt.AlignCenter) #CENTER & CENTER

def main():
    app = QApplication(sys.argv)            # crée l'app Qt
    window = MainWindow()                   # crée une instance de la fenêtre
    window.show()                           # affiche la fenêtre
    sys.exit(app.exec_())                   # lance la boucle principale de l'app


if __name__ == "__main__":
    main()