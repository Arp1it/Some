a =input("enter list with quamas:\n")
l = a.split(",")
# print(l)

b = int(input("1 for list 2 for set 3 for generator and 4 for dictionary: "))

if b == 1:
    li = [i for i in l]
    print(li)
    print(type(li))

if b == 2:
    st = {i for i in l}
    print(st)
    print(type(st))

if b == 3:
    ge = (i for i in l)
    for o in ge:
        print(o)
    print(type(ge))

if b == 4:
    dict1 = {f"item {i}": i for i in l}
    print(dict1)
    print(type(dict1))