import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))

        # Création d'un QLabel pour afficher l'image
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)       # Taille initiale de l'image dans le QLabel

        #Chargement de l'image dans un QPixmap
        pixmap = QPixmap("300px-YoshieggNSMBU.png")
        label.setPixmap(pixmap)                 # Affecte l'image au QLabel

        #Fait en sorte que l'imqage s'adapte à la taille du QLabel
        label.setScaledContents(True)

        # Centre du QLabel dans la fenêtre
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()