class Inspector:
    def __init__(self, fname, esalary, lname):
        self.name = fname
        self.salary = esalary
        self.lname = lname

    def __add__(self, other):
        return self.salary + other.salary

    def getmembers(self):
        return f"Modules name is add, lname, salary, name, __init__, getmembers"

arpit = Inspector("Arpit", 455, "Jaiswal")
ar = Inspector("Ar", 455, "Jaiswa")
# print(arpit + ar)
# print(arpit.getmembers())

import inspect 
# for item in inspect.classify_class_attrs(Inspector):
#     print(item)
# print(inspect.getmodule(arpit))
# print(inspect.classify_class_attrs(Inspector))
# print(inspect.getmembers(arpit)) 
print(inspect.getsource(Inspector))
print(inspect.getsource(Inspector.getmembers))