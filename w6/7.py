import os

WORKING_DIR = os.getcwd()

def safe_folder_create(path):
  if not os.path.exists(path):
    os.mkdir(path)
  else:
    print('path already exists')

os.chdir('dir1')

safe_folder_create('dir1_1')