# n = int(input("Enter number of names: "))
# names = []

# for i in range(n):
#     name = input("Enter name: ")
#     names.append(name.split(" "))

# print(names)

import random


def jumble_names():
    # If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
    # Thus in case of lname, even if someone has specified middle name it'll be considered as a whole
    fname = [name.split()[0] for name in names]
    lname = [name.split(" ", 1)[1] for name in names]

    for i in names:
        random_fname = random.choice(fname)
        random_lname = random.choice(lname)

        print(f"{random_fname} {random_lname}")

        fname.remove(random_fname)
        lname.remove(random_lname)


if __name__ == '__main__':
    n = int(input("Enter number of friends: "))
    names = []
    for i in range(n):
        names.append(input("Enter name of your friend: "))

    jumble_names()