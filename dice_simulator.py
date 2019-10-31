import random
print("Hi! This is a dice simulator.")

dice = random.randint(1,6)
y = "c"

while y == "c":
    if dice == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    if dice == 2:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")
    if dice == 3:
        print("---------")
        print("|   O   |")
        print("|   O   |")
        print("|   O   |")
        print("---------")
    if dice == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    if dice == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    if dice == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")
    y = input("press 'c' to roll again, or anything else to quit: ")
    dice = random.randint(1,6)
