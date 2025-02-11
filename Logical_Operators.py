# Logical operators = evaluate multiple conditions (or, and, not)
#                       or = at least one condition must be True
#                       and = both conditions must be True
#                       not = inverts the condition

temp = 3
is_raining = False
is_sunny = False

# OR statement
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")

#AND statement
if temp >= 28 and is_sunny:
    print("It's so HOT outside!")
    print("It's sunny!")
elif temp <= 0 and is_sunny:
    print("It's so COLD ouside!")
    print("It's sunny!")
elif 28 > temp > 0 and is_sunny:
    print("It's warm ouside.")
    print("It's sunny!")

#NOT statement
if temp >= 28 and not is_sunny:
    print("It's so HOT outside!")
    print("It's cloudy!")
elif temp <= 0 and not is_sunny:
    print("It's so COLD ouside!")
    print("It's cloudy!")
elif 28 > temp > 0 and not is_sunny:
    print("It's warm ouside.")
    print("It's cloudy!")



