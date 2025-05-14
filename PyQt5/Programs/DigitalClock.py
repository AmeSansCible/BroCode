import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# Pour gérer le temps (timer et l’heure actuelle)
from PyQt5.QtCore import QTimer, QTime, Qt

# Pour gérer les polices (typo personnalisée)
from PyQt5.QtGui import QFont, QFontDatabase


# Je crée une classe "DigitalClock" → c'est ma fenêtre (hérite de QWidget = simple fenêtre)
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()               # Obligatoire pour que la fenêtre fonctionne

        self.time_label = QLabel(self)   # Une étiquette qui affichera l’heure
        self.timer = QTimer(self)        # Un minuteur qui va déclencher des mises à jour

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Temps perdu")
        self.setGeometry(600, 400, 300, 100)

        # Crée un layout vertical
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)                # Ajoute l’étiquette dans le layout
        self.setLayout(vbox)                           # Applique le layout à la fenêtre

        self.time_label.setAlignment(Qt.AlignCenter)                 # Centre le texte de l’étiquette
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(122, 100%, 50%)")  # Style vert flashy
        self.setStyleSheet("background-color: black")                # Fond noir de la fenêtre

        # Charge une police spéciale (DS-DIGI.TTF) qui se trouve dans le dossier
        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]     # Récupère le nom
        my_font = QFont(font_family, 150)                                   # Crée une police taille 150
        self.time_label.setFont(my_font)                                    # Applique la police au label

        # On connecte le minuteur à une fonction → toutes les 1000ms (1 seconde), on actualise l’heure
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # On appelle la fonction une fois tout de suite pour que l’heure s’affiche direct
        self.update_time()

    def update_time(self):
        # Récupère l’heure actuelle au format hh:mm:ss
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)                       # Met à jour l’affichage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())