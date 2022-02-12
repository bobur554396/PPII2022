# - [ ] Inheritance

# all classes at the root will inherit from 'object'

class Person: 
  def __init__(self, _name, _age):  # constructor function -> magic method
    self.name = _name
    self.age = _age

  def __str__(self):
      return f'{self.name} - {self.age}'
  
  def show(self):
    print(f'{self.name} - {self.age}')


# Student - subclass/child
# Person - baseclass/superclass/parent
class Student(Person): 
  def __init__(self, _name, _age, _gpa, _id):
    super().__init__(_name, _age)
    self.gpa = _gpa
    self.id = _id
  
  # def __str__(self): # overriding the __str__ function from Person class
  #     return f'{self.name} - {self.age} - {self.gpa} - {self.id}'

  def __str__(self):
      return f'{super().__str__()} - {self.gpa} - {self.id}'


class Employee(Person):
  pass
  '''
  position
  wage
  department
  ...
  '''


s1 = Student('Student1', 20, 3.5, '21B111')
# s1.show()
print(s1)
