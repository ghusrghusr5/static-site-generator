from textnode import TextNode
from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive
import os, shutil



def main():
  src = "./static"
  dst = "./public"
  content = "./content"
  template_path = "./template.html"

  if os.path.exists(dst):
    shutil.rmtree(dst)
    print("Deleting public directory...")
  copy_files_recursive(src, dst)

  from_path = "./content"
  template_path = "./template.html"
  dest_path = "./public/"

  print("Generating page...")
  generate_pages_recursive(
    from_path,
    template_path,
    dest_path
    )


main()
