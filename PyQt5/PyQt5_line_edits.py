import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        self.button = QPushButton("Submit", self)               # Bouton avec le texte
        self.line_edit = QLineEdit(self)                        # Champ de texte pour écrire qqc

        self.initUi()

    def initUi(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)

        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")

        self.line_edit.setPlaceholderText("Enter your name")

        self.button.clicked.connect(self.submit)
    def submit(self):
        text = self.line_edit.text()                    # on récupère ce que l'utilisateur a écrit
        print(f"Hello {text}")                          # on affiche le message dans la console

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()