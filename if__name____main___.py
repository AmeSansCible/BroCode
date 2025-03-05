# if __name__ == __main__: (This script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing

# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)

#                           ex. library = Import library for functionnality
#                               When running library directly, display a help page

def main():
    # Your program goes here
    # Tout code qui ne doit pas s'exécuter lors d'un import doit aller dans main()
    # c'est le point d'entrée principal du programme

if __name__ == '__main__':
    main()