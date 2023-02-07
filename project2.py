number_of_inputs = int(input("enter number of items\n"))

ls = []
for i in range(number_of_inputs):
    en = input(f"item no {i}:\n")
    ls.append(en)

t = int(input("enter choice: \n"))

if t == 1:
    lis = [i for i in ls]
    print(list)

if t == 2:
    set = {m for m in ls}
    print(set)

if t == 3:
    gen = (k for k in ls)
    for c in gen:
        print(c)

if t == 4:
    f = {f"item {y}": y for y in ls}
    print(f)