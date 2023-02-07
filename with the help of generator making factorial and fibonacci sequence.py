def generator(i):
    for n in range(i):
        yield n

t = generator(int(input("enter range: ")))
m = input("enter operation:\n")

def fibonacci(t):
    for l in t:
        if l == 0:
            print(0)

        elif l == 1:
            print(l)
        
        else:    
            print((l-1)+(l-2))

def factorial(t):
    o = 1
    for l in t:
        o = o * (l+1)
    print(o)
        

if m == "fi":
    fibonacci(t)

if m == "fa":
    factorial(t)