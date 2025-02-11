# for loops = execute a block of code a fixed number of times.
#              You can iterate iver a range, string, sequence,...

for x in range(1, 11):
    print(x)


for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR")


for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)