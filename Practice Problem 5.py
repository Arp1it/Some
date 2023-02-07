try:
    user_input = int(input("Enter size of your list: "))
except Exception as e:
    print("please enter valid number only")
    exit()

a = []

for i in range(user_input):
    try:
        k = int(input())
    except Exception as e:
        print("please enter valid number only")
        exit()

    op = []
    op.append(k)
    
    for t in op:
        if t < 10:
            a.append(t)
        if t >= 10:
            while True:
                t += 1
                u = str(t)

                if str(t) == u[::-1]:
                    a.append(t)
                    break
print(a)