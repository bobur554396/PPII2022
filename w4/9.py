# Datetime
# import datetime
from datetime import datetime

# print(datetime.datetime.now())

now = datetime.now()

# print(now)
# print(now.day)
# print(now.year)
# print(now.month)
# print(now.strftime("%m:%Y:%d   %H:%M:%S  %a"))

now = datetime(2018, 3, 15)

print(type(now))
print(now.strftime("%A"))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
