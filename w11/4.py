with open('level1.txt', 'w') as f:
  for i in range(0, 500, 20):
    for j in range(0, 500, 20):
      f.write('*')
    f.write('\n')
