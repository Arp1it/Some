try:
    n = int(input("Please enter number of things: "))
    mn = int(input("Please enter minimum distribution number of thinsg: "))
    mx = int(input("Please enter maximum distribution number of things: "))
except Exception as e:
    print("Please enter int value only")
    exit()

if mn > mx:
    print("Maximum number is not smaller than minimum number please enter valid input only")
    exit()

while True:
    if n%mn == 0:
        print(f"{mn} is a divisor of {n}")

    if n%mn != 0:
        print(f"{mn} is not a divisor of {n}")

    if mn == mx:
        break

    mn += 1