# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2.except, 3.finally


try:                                            # on essaie de faire qqc de risqué
    number = int(input("Enter a number:"))
    print(1 / number)
except ZeroDivisionError:                       # si une erreur se produit, on l'attrape ici
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:                               # attrape toutes les autres erreurs non prévues
    print("Something went wrong")
finally:                                        # ce bloc s'exécute toujours, erreur ou pas!
    print("Do some cleanup here!")
