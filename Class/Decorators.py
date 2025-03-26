# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):               # *args, **kwargs permet de gérer n’importe quel argument
        print("*You add sprinkles*")            # Action avant la fonction
        func(*args, **kwargs)                   # Appel de la vraie fonction
    return wrapper                              # On retourne la fonction "enrobée"


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper


# Fonction de base qu’on veut décorer
@add_sprinkles     # Sera exécuté EN DERNIER (à l’extérieur)
@add_fudge         # Sera exécuté EN PREMIER (le plus proche de la fonction)
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")


get_ice_cream("vanilla")
