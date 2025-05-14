import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Création des widgets (éléments visuels)
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        # Mise en page verticale
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Centrage des widgets
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Attribution d'un nom aux widgets (utile pour appliquer des styles précis)
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Personnaliser l'apparence
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        # Connexion du bouton à la méthode qui récupère la météo
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # Clé API pour OpenWeatherMap (à sécuriser dans une vraie appli)
        api_key = "501639011e56256b12e4baf7e574c7c5"

        # Récupération du nom de la ville depuis le champ texte
        city = self.city_input.text()

        # URL de requête à l'API météo
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        # Bloc try...except qui évite que le programme ne plante : en cas d'erreur -> message informatif -> app reste ouverte
        # try: code qui peut poser problème
        # except ErreurSpécifique: réaction adaptée (affichage d'un message ou action alternative)

        # try:
        #     Envoie la requête à l'API météo
        #     Si tout va bien :
        #         lire la réponse, convertir le JSON, afficher
        #     Sinon :
        #         raise_for_status() déclenche une erreur
        # except:
        #     Rattrape l'erreur et affiche un message clair pour l'utilisateur

        try:
            response = requests.get(url)                                      # Envoi de la requête HTTP
            response.raise_for_status()                                       # Déclenche une erreur (HTTPError) si la réponse du serveur contient un code d'erreur (comme 404, 500, etc.).

            data = response.json()                                            # Conversion de la réponse JSON en dictionnaire Python

            if data["cod"] == 200:
                self.display_weather(data)                                    # Affiche les données si tout s'est bien passé

        # Gestion des erreurs HTTP spécifiques avec des messages explicites
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        # Gestion des autres types d'erreurs réseau
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")



    # Affiche un message d'erreur dans le label de température
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)                   # Affiche le message
        self.emoji_label.clear()                                  # Efface l’emoji
        self.description_label.clear()                            # Efface la description

    # Affiche les données météo obtenues via l'API
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")        # Remet la taille standard (modifiée en cas d'erreur sinon)

        temperature_k = data["main"]["temp"]                            # Température en Kelvin
        temperature_c = temperature_k - 273.15                          # Conversion en Celsius

        weather_id = data["weather"][0]["id"]                           # Code météo (pour déterminer le type de temps)
        weather_description = data["weather"][0]["description"]         # Description textuelle du temps

        self.temperature_label.setText(f"{temperature_c:.1f}°C")        # Affiche la température formatée
        self.emoji_label.setText(self.get_weather_emoji(weather_id))    # Affiche l'emoji météo
        self.description_label.setText(weather_description.capitalize())  # Affiche la description avec majuscule

    # Méthode statique qui retourne un emoji en fonction du code météo
    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌁"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return







if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())