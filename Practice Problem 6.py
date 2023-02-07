import random

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# v = int(input("enter how many player play this game: "))

c = random.randint(a, b)
# print(c)
e = 1
f = 1

i = 1
g = 0
while True:
    d = int(input(f"Player{i} chance: "))

    if d < c:
        print("Wrong input your input number is smaller.")
        g += 1
        

    if d > c:
        print("Wrong input your input number is greater.")
        g += 1 
        continue

    if d == c:
        print(f"After {g} chance you guess right number")
        # if i > 0 and i < v:
        if i == 1:
            e += g
            g *= 0
            i += 1
            c = random.randint(a, b)
            continue

        # if i == v:
        if i == 2:
            f += g
            g *= 0
            if e < f:
                print(f"Player1 is win because Player2 guess number in {e} chances")
                break

            if e > f:
                print(f"Player2 is win because Player1 guess number in {f} chances")
                break

            if e == f:
                print("Draw both player guess number in equal chances")
                print(i)
                break