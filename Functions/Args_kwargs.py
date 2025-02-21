# *args     = allows you to pass multiple non-key arguments -> tuple
# **kwargs  = allows you to pass multiple keyword-arguments -> dictionary
#             * unpacking operator
#             1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Spongebob", "Harold", "Squarepants", "III")

print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake street",
              apt="100",
              city="Detroy",
              state="Michigan",
              zip="54321")

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr", "Spongebob", "Squarepants", "III",
               street="123 Fake Street",
               pobox="PO box #100",
               city="Detroit",
               state="MI",
               zip="54321")

