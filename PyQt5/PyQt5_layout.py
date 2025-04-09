import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("300px-YoshieggNSMBU.png"))
        self.initUI()

    #Création du widget central qui va contenir la mise en page
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # --- Optionnel : On pourrait utiliser un VBoxLayout ici à la place du grid ---

        # vbox = QVBoxLayout()
        #
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        #Création d'une grille pour disposer les labels
        grid = QGridLayout()

        # Placement des labels dans la grille (ligne, colonne)
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        # applique le layout au widget central
        central_widget.setLayout(grid)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()