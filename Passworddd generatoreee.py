import string
import random

a1 = string.ascii_lowercase
a2 = string.ascii_uppercase
a3 = string.digits
a4 = string.punctuation

try:
    b = int(input("enter length of password integer accept only:\n"))
except Exception as c:
    print("OOPs, enter int value only")
    # print(c)

# except ValueError:
#     print("oops")

a = []
a.extend(a1)
a.extend(a2)
a.extend(a3)
a.extend(a4)

try:
    print("Your password is-", "".join(random.sample(a, b)))
except Exception as d:
    print("wrong")

try:
    random.shuffle(a)
    print("Your password is-", "".join(a[0:b]))
except Exception as l:
    print("")