class Employee():
    no_of_leaves = 8

    def __init__(self, aname, bsalary, crole):
        self.name = aname
        self.salary = bsalary
        self.role = crole

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
harry = Employee("Harry", 4554, "Instructor")
rohan = Employee("Rohan", 454, "Student")

harry.change_leaves(34)

# print(harry.printdetails())
print(harry.no_of_leaves)
print(Employee.no_of_leaves)