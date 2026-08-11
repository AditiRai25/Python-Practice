# Demonstrate polymorphism using the same method name

class Dog:
    def sound(self):
        print("Dog makes a sound.")


class Cat:
    def sound(self):
        print("Cat makes a sound.")


for animal in [Dog(), Cat()]:
    animal.sound()
