# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional, 2. default, 3.KEYWORD, 4.arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", last="Code", first="Bro")   # l'ordre peut être modifié facilement
                                                                # Attention : positional argument BEFORE keyword argument

for x in range(1,11):
    print(x, end=" ")                                           # end= est un keyword argument

print("1", "2", "3", "4", "5", sep="-")                         # sep= est un keyword argument

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)