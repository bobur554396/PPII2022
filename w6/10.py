import os

WORKING_DIR = os.getcwd()


def safe_folder_create(path):
  if not os.path.exists(path):
    os.mkdir(path)
  else:
    print('path already exists')

# os.makedirs('f1/f2/f3')


for root, dirs, files in os.walk('.'):
  print(root)
  print(f'dirs: {dirs}')
  print(f'files: {files}')
  print('----'*10)
