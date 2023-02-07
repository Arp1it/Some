class Employee():
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 10
print(Employee.__dict__)
print(rohan.__dict__)

Employee.no_of_leaves = 9
print(Employee.no_of_leaves)
print(Employee.__dict__)
print(rohan.__dict__)
print(harry.__dict__)