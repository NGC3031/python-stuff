class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Bob", 32)
p3 = Person("Max", 35)
p4 = Person("Sam", 26)
p1.myfunc()
p2.myfunc()
p3.myfunc()
p4.myfunc()
