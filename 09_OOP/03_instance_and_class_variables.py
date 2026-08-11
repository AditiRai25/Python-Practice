# Demonstrate instance and class variables

class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Aditi")
student2 = Student("Rahul")

print("Student 1:", student1.name)
print("Student 2:", student2.name)
print("College:", Student.college)
