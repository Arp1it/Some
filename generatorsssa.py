"""
iterable - __iter__() or __getitem__()
iterator - __next__()
iteration - 
"""

def gen(n):
    for i in range(n):
        yield i

l = gen(36)

# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())

# for i in l:
#     print(i)

a = "arpit"

ier = iter(a)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# print(a.__iter__())

# print(a[0])

# for c in a:
#     print(c)