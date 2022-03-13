import os

WORKING_DIR = os.getcwd()

def safe_folder_create(path):
  if not os.path.exists(path):
    os.mkdir(path)
  else:
    print('path already exists')

# print(os.path.exists('dir1'))
# os.mkdir('dir1')


safe_folder_create('dir2')

# print(WORKING_DIR)
