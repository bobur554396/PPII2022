# a = input('Enter list of numbers...\n')

# nums = a.split(' ')

# sum = 0
# for n in nums:
#   sum += int(n)


a = [float(n) for n in input('Enter list of numbers...\n').split(' ')]

print([i * 2 for i in a])
print(a)
