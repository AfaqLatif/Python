
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
        

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

e1=Employee("Ali", 255, "Instructor")
e2=Employee("Ammar", 455, "Student")
e3=Employee.from_dash("Kiara-480-Student")

print(e1.printdetails())
print(e2.printdetails())
print(e3.printdetails())

Employee.printgood("Umar")

