# def function1():
#     print("hello sir")

# func2 = function1()
# del function1
# func2

# def funcret(num):
#     if num == 0:
#         return print

#     if num == 1:
#         return sum

# a = funcret(1)
# print(a)

# def executor(func):
#     func("This")

# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec

# without decorator
def whoisharry():
    print("Harry is a good boy")

whoisharry = dec1(whoisharry)
whoisharry()

# using decorator
@dec1
def whoisharry1():
    print("Harry is a good boy")

whoisharry1()