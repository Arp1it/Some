items = ["hello", "arpit", "akshansh", "harry", "1", "2"]
o = input("enter:\n")

for item in items:
    if o == item:
        print(f"{o} is present")
        break

else:
    print(f"{o} is not present")