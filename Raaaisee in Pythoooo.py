# a = input("What is your name: ")
# b = input("How much do you earn: ")

# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 so stopping the programme")

# if a.isnumeric():
#     raise Exception("Numbers are not allowed")

# print(f"Hellow {a}")

c = input("Enter your name: ")

try:
    print(a)

except Exception as e:
    if c == "harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exceptioin handle")
    print(f"name is - {c}")