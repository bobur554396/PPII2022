n = int(input())

arr = []
for i in range(n):
  num = [int(n) for n in input().split(' ')]
  arr.append(num)
  

for row in arr:
  print(row)
