# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = coma separator

price1 = 3005.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is €{price1:.2f}") # arrondit à 2 décimales
print(f"Price 1 is €{price2:10}") # alloue 10 espaces au numéro
print(f"Price 1 is €{price3:>10}") # alloue 10 espaces et justifie à droite
print(f"Price 1 is €{price1: }") # insert un espace avant un nbre positif
print(f"Price 1 is €{price1:,}") # insert une , pour séparer les milliers
print(f"Price 1 is €{price1:^15}") # justifie au centre dans les 15 "cases" allouées
print(f"Price 1 is €{price1:+,.2f}") # possibilité de combiner