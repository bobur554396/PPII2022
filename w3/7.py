class Person:
  name = 'Student1'
  age = 20
  
  def show(self): # instance method / function
    print(f'{self.name} - {self.age}')

p = Person() # object / instance of the class Person

p.age = 22
p.show()

# print(p.name)
# print(p.age)

p2 = Person()
p3 = Person()
