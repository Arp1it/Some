a = input("Enter the items with quamas: ")
a = a.replace(" ", "")
b = a.split(",")

# REVERSE LIST USING SLICING
c = b[::-1]
print(c)

# Reverse list with inbuilt function in python
l = b[:]
l.reverse()
print(l)

# REVERSE LIST USING SWAP METHOD
p = len(b)- 1
for i in range(len(b)//2):
    b[i], b[p-i] = b[p-i], b[i]
print(b)