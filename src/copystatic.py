import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
      os.mkdir(dest_dir_path)

    for file_name in os.listdir(source_dir_path):
      src_path = os.path.join(source_dir_path, file_name)
      dst_path = os.path.join(dest_dir_path, file_name)
      print(f" * {src_path} -> {dst_path}")
      if os.path.isfile(src_path):
        shutil.copy(src_path, dst_path) # do it with copytree next time
      else:
        copy_files_recursive(src_path, dst_path)
