from datetime import date

today = date.today()

class Library:
    def __init__(self):
        with open("books.txt", "w") as f:
            pass

        with open("history.txt", "w") as f:
            pass

        with open("lend.txt", "w") as f:
            pass

    def Check_history(self):
        passwordd = input("enter password to access history of all users: ")

        if passwordd == "__12user_his":
            with open("history.txt") as q:
                print("\nHistory of all user accesed:---")
                i = q.read().split("\n")

            for l in i:
                print(f" {l}")

        else:
            print("wrong password")

    def printbooks(self):
        print("Names of books are -")
        with open("books.txt") as filename:
            filenames = filename.read().split(",")

        for books in filenames:
            print(books)

    def lendbooks(self):
        a = input("What is your name:\n")
        b = input("enter book name:\n")

        with open("books.txt") as r:
            file = r.read().split(",")

        if b in file:
            with open("books.txt") as e:
                c = e.read()

            coi = c.replace(f"{b},", "")

            with open("books.txt", "w") as l:
                n = l.write(coi)

            with open("books.txt") as filename:
                filenames = filename.read().split(",")

            for books in filenames:
                print(books)

            with open("lend.txt", "a") as f:
                a = f.write(f"{a} lend book which book name is {b}\n")

            print("done")

            with open("history.txt", "a") as h:
                h.write(f"{a} lend {b} book -- {today} \n") 

        elif b not in file:
            print("not found")
                

    def addbooks(self):
        c = input("Enter books name using quamas:\n")

        with open("history.txt", "a") as h:
            h.write(f"add {c} book -- {today} \n")

        with open("books.txt", "a") as s:
            w = s.write(f"{c},")

        with open("books.txt") as filename:
            filenames = filename.read().split(",")

        for books in filenames:
            print(books)

        print("done")

    def returnbooks(self):
        f = input("enter your name:\n")
        g = input("enter book name:\n")

        with open("lend.txt") as re:
            d = re.read().split("\n")

        if f"{f} lend book which book name is {g}" in d:
            with open("lend.txt", "r") as e:
                co = e.read()

            coin = co.replace(f"{f} lend book which book name is {g}\n", "")

            with open("lend.txt", "w") as l:
                on = l.write(coin)

            with open("books.txt", "a") as s:
                w = s.write(f"{g},")

            with open("books.txt") as filename:
                filenames = filename.read().split(",")

            for books in filenames:
                print(books)

            print("done")

            with open("history.txt", "w+") as h:
                h.write(f"{f} return {g} book -- {today} \n")

        else:
            print("notfound")

ar = Library()
print("welcome to my library")

while True:
    print("(add: for add books)\n(booksname: for check bokk name in library)\n(rebooks: for return books)\n(lend: for lendbooks)\n(checkhis: for check history)\n(q: for quit)")
    e = input("enter what you want:\n")

    try:
        if e == "lend":
            ar.lendbooks()
    except Exception as a:
        print("book is not available")

    # if e == "lend":
    #    ar.lendbooks()

    if e == "add":
        ar.addbooks()

    if e == "booksname":
        ar.printbooks()

    if e == "rebooks":
        ar.returnbooks()

    if e == "checkhis":
        ar.Check_history()

    if e == "q":
        break

    else:
        print("please enter valid input!!!")