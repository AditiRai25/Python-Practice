# Demonstrate constructor using __init__

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Aditi", "B.Sc IT")
student1.display()
