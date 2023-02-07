a = int(input("Enter nuber: "))
l = ''

for i in range(a):
    try:
        t = int(input())
    except Exception as e:
        print("please enter valid number")

    m = str(t)
    u = str(t)

    if str(t) == u[::-1]:
        l += f"{m} is a palindrome of itself\n"

    # print(u[::-1])
    while True:
        t += 1
        u = str(t)
        # print(u[::-1], t)

        if str(t) == u[::-1]:
            l += f"Next palindrome of {m} is {t}\n"
            break

print(l)


# reverse_num = 0
# u = 451
# while u>0:
#     remainder = u % 10
#     reverse_num = (reverse_num * 10) + remainder
#     u = u//10

# print(reverse_num)
