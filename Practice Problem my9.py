try:
    n = int(input("enter how many friends name you eant to enter: "))
except Exception as e:
    print("enter integer value only")
    exit()

fname = []
lname = []

for i in range(n):
    a = input("enter friend name: ")

    fname.append(a.split()[0])
    try:
        lname.append(a.split(" ", 1)[1])
    except Exception as e:
        print("please enter valid only and surname also")
        exit()

print(fname, lname)
d = lname[::-1]

for i, st in enumerate(fname):
    print(st, d[i])