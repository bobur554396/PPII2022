import os

WORKING_DIR = os.getcwd()


def safe_folder_create(path):
  if not os.path.exists(path):
    os.mkdir(path)
  else:
    print('path already exists')


def align_left(depth):
  print('   ' * depth, end=' ')

def show_dir_content(path, depth = 1):
  for item in os.listdir(path):
    target_path = os.path.join(path, item)
    if os.path.isfile(target_path):
      align_left(depth)
      print(f'FILE: {item}')
    if os.path.isdir(target_path):
      align_left(depth)
      print(f'DIR: {item}')
      show_dir_content(target_path, depth + 2)


os.chdir('..')
new_path = os.getcwd()

# show_dir_content(WORKING_DIR)
show_dir_content(new_path)
