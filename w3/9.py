class Person:
  def __init__(self, _name, _age):  # constructor function -> magic method
    self.name = _name
    self.age = _age
  
  def __str__(self):
      return f'{self.name} - {self.age}'

p = Person('Student_11', 22)
print(p)

# a = 2
# print(a) # -> toString --> __str__