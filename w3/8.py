class Person:
  def __init__(self, _name, _age): # constructor function -> magic method
    self.name = _name
    self.age = _age
  
  def show(self):
    return f'{self.name} - {self.age}'


p = Person('Student_11', 22)
print(p.show())

p2 = Person('Student_22', 20)
print(p2.show())
