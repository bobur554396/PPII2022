import os

WORKING_DIR = os.getcwd()


def safe_folder_create(path):
  if not os.path.exists(path):
    os.mkdir(path)
  else:
    print('path already exists')


# print(os.path.isdir('/Users/bobur/Desktop/examples/PPII2022/w6/input2.txt'))
# print(os.path.isfile('/Users/bobur/Desktop/examples/PPII2022/w6/input2.txt'))

for item in os.listdir(WORKING_DIR):  # os.listdir('.')
  # target_path = WORKING_DIR + item # not recommended
  target_path = os.path.join(WORKING_DIR, item)
  if os.path.isdir(target_path):
    print(f'DIR: {item}')
    for item2 in os.listdir(target_path):
      print('---'*2, item2)
  if os.path.isfile(target_path):
    print(f'FILE: {item}')
