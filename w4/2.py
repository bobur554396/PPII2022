class MyNumber:
  def __iter__(self):
    self.x = 1
    return self

  def __next__(self):
    if self.x > 7:
      raise StopIteration
    
    x = self.x
    self.x += 1
    return x

my_num = MyNumber()

for i in my_num:
  print(i)
