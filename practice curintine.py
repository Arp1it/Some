def serving():
    import time
    Name_list = "Arpit, Harry, Yash, Hardik, Divesh, Nagesh, Akshansh, etc"
    # Any task which consume time
    time.sleep(5)

    while True:
        tex = (yield)

        if tex in  Name_list:
            print(f"Yes {n} name is in namelist at {Name_list.find(n)}")

        if tex not in Name_list:
            print("Your name not in list sorry")

# serve = serving()
while True:
    serve = serving()
    n = input("Please enter your name: ")
    print("Search started")
    next(serve)
    serve.send(n)

    i = input("continue or not y or n:\n")

    if i == "y":
        serve.close()
        continue

    if i == "n":
        print("Thank you")
        serve.close()
        break