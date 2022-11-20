# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)
# # bypass error
# pass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name = input("Enter your name ")
age = input("Enter your age ")
        
# # p1 = Person("john",87)
# p1 = Person(name, age)
# print(p1.name)
# print(p1.age)

p1 = Person("john",87)
del p1
print(p1)