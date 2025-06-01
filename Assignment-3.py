# 1. Class with name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Alice", 30)
print("1.", p1.name, p1.age)

# 2. Greeting method:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}.")
p2 = Person("Bob", 25)
print("2.", end=' ')
p2.greet()

# 3. Class and instance variables:
class Example:
    class_var = "ClassVar"
    def __init__(self, value):
        self.instance_var = value
e = Example("InstanceVar")
print("3.", Example.class_var, e.instance_var)

# 4. Private attribute access:
class Secret:
    def __init__(self):
        self.__hidden = "Private"
    def reveal(self):
        return self.__hidden
s = Secret()
print("4.", s.reveal())

# 5. Square of number:
class Math:
    def square(self, x):
        return x * x
m = Math()
print("5.", m.square(4))

# 6. Two independent objects:
class Counter:
    def __init__(self):
        self.count = 0
a = Counter()
b = Counter()
a.count += 1
b.count += 2
print("6.", a.count, b.count)

# 7. Method to set attributes:
class Student:
    def set_info(self, name, grade):
        self.name = name
        self.grade = grade
st = Student()
st.set_info("Tom", "A")
print("7.", st.name, st.grade)

# 8. isinstance demo:
class Animal:
    pass
dog = Animal()
print("8.", isinstance(dog, Animal))

# 9. Single inheritance:
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    pass
print("9.", end=' ')
Dog().speak()

# 10. Multi-level inheritance:
class A:
    def method_a(self):
        print("A")
class B(A):
    def method_b(self):
        print("B")
class C(B):
    def method_c(self):
        print("C")
print("10:")
obj = C()
obj.method_a()
obj.method_b()
obj.method_c()

# 11. Method overriding:
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        print("Hello from Child")
print("11:", end=' ')
Child().greet()

# 12. Use super():
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
print("12:")
Child().greet()

# 13. Abstract base class:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return 3.14 * 2 * 2
print("13.", Circle().area())

# 14. Multiple inheritance:
class A:
    def method_a(self):
        print("A")
class B:
    def method_b(self):
        print("B")
class C(A, B):
    pass
print("14:")
multi = C()
multi.method_a()
multi.method_b()

# 15. Encapsulation with getter/setter:
class Person:
    def __init__(self):
        self.__age = 0
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
p = Person()
p.set_age(40)
print("15.", p.get_age())

# 16. Polymorphism example:
class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Woof")
def animal_sound(animal):
    animal.speak()
print("16:")
animal_sound(Cat())
animal_sound(Dog())

# 17. Employee count:
class Employee:
    count = 0
    def __init__(self):
        Employee.count += 1
    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.count}")
e1 = Employee()
e2 = Employee()
print("17:", end=' ')
Employee.display_count()

# 18. Constructor overloading:
class Demo:
    def __init__(self, x=0, y=0):
        self.sum = x + y
d1 = Demo(3, 4)
d2 = Demo(5)
print("18.", d1.sum, d2.sum)

# 19. Bank account system:
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
acc = BankAccount()
acc.deposit(100)
acc.withdraw(40)
print("19.", acc.balance)

# 20. Rectangle area and perimeter:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
r = Rectangle(5, 3)
print("20. Area:", r.area(), "Perimeter:", r.perimeter())
