import psycopg2


conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="pp2demo_user",
  password="passw0rd")


sql = 'select * from students where gpa > 3.5'

cursor = conn.cursor()
cursor.execute(sql)

students = cursor.fetchall()

print(students)

cursor.close()
conn.close()
