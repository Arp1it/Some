# li = []

# for i in range(100):
#     if i%3 == 0:
#         li.append(i)

# print(li)

# ls = [i for i in range(100) if i%3 == 0]
# print(ls)

# dict1 = {i:f"item {i}" for i in range (1, 1000) if i%100 == 0}
# dict1 = {i:f"Item {i}" for i in range (6)}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict1, "\n", dict2)

# dresses = {dress for dress in ["dress1", "dress2","dress1", "dress2", "dress1", "dress2"]} 
# print(dresses)

b = 101
evens = (i for i in range(b) if i%2 == 0)
# print(evens.__next__())

for l in evens:
    print(l)