# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):       # constructeur (qui fabrique l'objet)
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):                                  # c'est ce que python affiche quand tu print ton objet
                                                        # c'est l'étiquette collée dessus quand tu veux afficher l'objet
        return f"{self.title} by {self.author}"

    def __eq__(self, other):                             # __eq__ = égalité ==
                                                         # Appelée quand on compare deux objets avec ==
                                                         # Ici, deux livres sont "égaux" s’ils ont le même titre ET le même auteur
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):                             # __lt__ = inférieur <
                                                         # Appelée quand on compare avec <
                                                         # Ici, on compare le nombre de pages
        return self.num_pages < other.num_pages

    def __gt__(self, other):                             # __gt__ = supérieur >
                                                         # Appelée quand on compare avec >
                                                         # Pareil, comparaison sur le nombre de pages
        return self.num_pages > other.num_pages

    def __add__(self, other):                            # __add__ = addition +
                                                         # Appelée quand on fait obj1 + obj2
                                                         # Ici, on additionne le nombre de pages des deux livres
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):                     # __contains__ = mot-clé in objet
                                                         # Appelée quand on fait 'mot' in obj
                                                         # Ici, on cherche si le mot est dans le titre ou l’auteur
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):                          # __getitem__ = accès par indice / clé
                                                         # Appelée quand on fait obj['clé']
                                                         # Permet d’accéder à certaines infos comme dans un dictionnaire
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"


book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "J-K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)


print(book1)
print(book1 == book2)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print("Lion" in book3)
print(book1["title"])