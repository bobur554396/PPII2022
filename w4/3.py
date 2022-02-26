class Fib:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        self.y = 1
        self.cnt = 1
        return self

    def __next__(self):  # 3 5
        if self.cnt > self.limit:
            raise StopIteration

        x, y = self.x, self.y
        self.x, self.y = self.y, self.x + self.y
        self.cnt += 1
        return x + y


a = Fib(5)
for i in a:
  print(i)