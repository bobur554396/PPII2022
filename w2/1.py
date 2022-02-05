n = int(input('Enter any number...\n'))

if n % 2 == 0:
  print('even')
  if n % 4 == 0:
    print('number is good')
elif n == 11:
  print('it is 11')
else:
  print('odd')
