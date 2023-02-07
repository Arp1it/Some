class library:
    def display(self, name):
        print("Welcome to"+name, end = "")
    def lend(self, list):
        print("Which book do you want?")
        a = input()
        print("tell your name")
        name = input()
        f = open("logs.txt","a")
        f.write("The person is :" +name+"\n")
        print(f"{a} is now with you {name}")
        return f"{list.remove(a)}"
    def add(self,list):
        print("Write the name you want to add")
        a = input()
        print("Succesfully added")
        return list.append(a)
    def retn(self,list):
        print("What do you want to return")
        a = input()
        print("Your name")
        name = input()
        print("Done")
        return list.append(a)

# Main Code
World_Library = library()
mainlist = [ "In Search of Lost Time","Ulysses","Don Quixote","The Great Gatsby","Harry Potter"]
World_Library.display(" 'World Library' ")
print(mainlist)
while True:
        print("What do you want to do")
        do = input()
        if do == "lend":
            World_Library.lend(mainlist)
        elif do == "add":
            World_Library.add(mainlist)
        elif do == "return":
            World_Library.retn(mainlist)