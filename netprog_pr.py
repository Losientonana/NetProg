class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)  
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID


employee = Employee("IoT", 25, 1508)


print("이름:", employee.getName())
print("나이:", employee.getAge())
print("ID:", employee.getID())
