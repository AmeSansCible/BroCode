import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # fenêtre principale
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        # création du bouton
        self.button = QPushButton("Click me", self)

        # création du label
        self.label = QLabel("Hello", self)              # "self." crée un label stocké dans l’objet pour pouvoir le retrouver plus tard
                                                        # sans "self." ça crée une variable temporaire locale à la fonction
        #initialisation de l'interface
        self.initUI()

    def initUI(self):
        # position et style du bouton
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")

        # connexion du bouton à la méthode "on_click"
        self.button.clicked.connect(self.on_click)

        # position et style du label
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 50px;")


    def on_click(self):
        self.label.setText("Goodbye")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()