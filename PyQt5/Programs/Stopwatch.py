import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time =QTime(0, 0, 0, 0)                    # initialise le temps à 0

        # Création des éléments de l'interface
        self.time_label = QLabel("00:00:00:00", self)   # Affiche le temps
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.timer = QTimer(self)                       # QTimer pour déclencher une màj régulière de l'affichage

        self.initUI()                                   # initialisation de l'interface utilisateur


    def initUI(self):
        self.setWindowTitle("Stopwatch")        # Change le nom de la fenêtre

        # Layout principal
        vbox = QVBoxLayout()                    # Crée le layout vertical
        vbox.addWidget(self.time_label)         # Ajoute les widgets dans le layout

        self.setLayout(vbox)                    # Applique le layout à la fenêtre

        self.time_label.setAlignment(Qt.AlignCenter)      # Centre le time_label

        hbox = QHBoxLayout()                    # Crée un layout horizontal

        hbox.addWidget(self.start_button)       # Ajoute les widgets au layout horizontal
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)                    # Ajoute le layout horizontal au layout vertical

        self.setStyleSheet("""
        QPushButton, QLabel{
            padding: 20px;
            font-weight: bold;
            font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(199, 75%, 68%);
                border-radius: 20px;
            }       
        """)

        # Conncexion des signaux aux fonction associées
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # à chaque "tick" du timer, on met à jour l'affichage
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)                # Démarre le timer avec un intervalle de 10ms

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()                                       # stoppe le timer
        self.time = QTime(0, 0, 0, 0)                           # Réinitialise le temps à 0
        self.time_label.setText(self.format_time(self.time))    # Met à jour l'affichage

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10                        # on passe de 3 digits à 2 en divisant par 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)        # on met à jour le temps avec + 10 millisecondes
        self.time_label.setText(self.format_time(self.time))    # on met à jour le label



if __name__ == "__main__":
    app = QApplication(sys.argv)     # Crée une instance de l'application Qt
    stopwatch = Stopwatch()          # Crée l'instance de notre widget Stopwatch
    stopwatch.show()                 # Affiche la fenêtre à l'écran
    sys.exit(app.exec_())            # Lance la boucle principale de l'application