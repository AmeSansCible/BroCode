# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global (outside of any function) -> Built-in

def func1():
    a = 1       # la variable a est locale à la fonction 1, les fonctions ne peuvent pas voir à l'intérieur des autres fonctions
    print(a)

def func2():
    b = 2
    print(b)



def func1():
    x = 1       # la variable est enclosed
    def func2():
        x = 2
        print(x)
    func2()



def func1():
    print(x)

def func2():
    print(x)

x = 3           # la variable est en dehors des fonctions, elle est globale
func1()
func2()
# s'il n'y a pas de variable locale et enclosed, alors il ira chercher en global



from math import e

def func1():
    print(e)        # la variable est built-in


func1()
