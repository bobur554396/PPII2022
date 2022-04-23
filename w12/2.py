import psycopg2


conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="pp2demo_user",
  password="passw0rd")


name = input('Eneter your name...\n')

sql = f'select id, email, score from students where name = \'{name}\''

cursor = conn.cursor()
cursor.execute(sql)

students = cursor.fetchall()

if len(students) > 0:
  print(f'Welcome {students[0][1]}! You last score = {students[0][2]}')
  # print('you already registered in the system')
else:
  print('please register in the system')



cursor.close()
conn.close()