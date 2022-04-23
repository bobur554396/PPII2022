import psycopg2
import random


conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="pp2demo_user",
  password="passw0rd")


sql = 'select * from students where gpa > 3.5'



students = [
  f'({random.randint(4, 100)}, \'{f"student{i}"}\', \'{f"email{i}@gmail.com"}\', {random.randint(1, 5)})'
  for i in range(1000)
]

insert_sql = f"insert into students (id, name, email, gpa) values {', '.join(students)};"


cursor = conn.cursor()
cursor.execute(insert_sql, insert_sql)

conn.commit()


cursor.close()
conn.close()


