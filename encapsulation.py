#Encapsulation-uses access modifiers and getter and setter methods

#Public variables and methods-can be accessed by any part of program
class Rectangle:
    length = 8
    breadth = 12

    def area(self):
        return self.length * self.breadth

r = Rectangle()
print(r.area())

#Getter and Setter methods-used to access and modify private variables in a class
class Person:
    __name = "Peligro"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person()
print(p.get_name())
p.set_name("Sanchez")
print(p.get_name())

