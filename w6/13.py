import csv

with open('test.csv', 'w') as f:
  writer = csv.writer(f, delimiter=',')
  for i in range(5):
    writer.writerow([f'name: {i}', f'age: {i}', f'address: {i}'])
  
  # writer.writerows([[..]])
