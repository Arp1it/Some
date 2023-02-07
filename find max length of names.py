# class Solution:
#   def longest(self, names, o):
      
#     mak = names[0]
#     for i in range (1,o) :
            
#       if len(mak) < len(names[i]):
#         mak = names[i]
           
           
#     return mak

class Solve():
  def long(self, names, o):
    k = ""

    for i in names:
      if len(i) > len(k):
        k = i

    return k

a = Solve()
name = ["3", "4", "sf", "rferg", "fqergqergqg", "fddfv", "dfgewrgwrgrwgwtgwegt"]
print(a.long(name, 6))