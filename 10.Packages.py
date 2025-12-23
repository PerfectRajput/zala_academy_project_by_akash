project/
│
├── mypackage/
│   ├── __init__.py
│   ├── class_one.py
│   └── class_two.py
│
└── main.py
# class_one.py

class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Student name is:", self.name)






# class_two.py

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def show_id(self):
        print("Employee ID is:", self.emp_id)

 
# __init__.py

from .class_one import Student
from .class_two import Employee

 
# main.py

from mypackage import Student, Employee

# Creating object of Student class
student1 = Student("Arpit")
student1.show_name()

# Creating object of Employee class
employee1 = Employee(101)
employee1.show_id()
