#     - [ ] open method (read - r / append - a / write - w / create - x)

f = open('input.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# for line in f.readlines():
#   print(line)

for line in f:
  print(line)
  
f.close() # close the stream/IOWrapper