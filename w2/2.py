line = input('Enter any word..\n')

# print(len(line))
# print(line[0]) # [start:end:step]

# 1) 
# for c in line:
#   print(c)


# 2)
# for index, val in enumerate(line):
#   print(f'{index} -> {val}')

# 3) 
# for i in range(len(line)):  # [start:end:step]
#   print(line[i])


i = 0
while i < len(line):
   print(line[i])
   i += 1
