# Python weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pounds (K/L)? :")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"{unit} is not a valid unit.")

print(f"Your weight is : {round(weight, 2)} {unit}.")


