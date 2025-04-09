import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "yoshi trap remix.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("IT'S TIIIIME!")

            pygame.mixer.init()                         # initialise le système audio de pygame
            pygame.mixer.music.load(sound_file)         # charge le fichier audio
            pygame.mixer.music.play()                   # Lance la lecture du fichier audio. Si on s'arrête là le fichier audio s'arrête dès que le programme s'arrête (~1sec après)

            while pygame.mixer.music.get_busy():        # Cette boucle continue tant que la musique est en cours de lecture
                time.sleep(1)                           # attend une seconde entre chaque vérification


            is_running = False                          # quand la musique est terminée on sort de la boucle

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)