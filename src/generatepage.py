from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for file in os.listdir(dir_path_content):
    from_path = os.path.join(dir_path_content, file)
    dest_path = os.path.join(dest_dir_path, file)
    if os.path.isfile(from_path):
      dest_path = Path(dest_path).with_suffix(".html")
      generate_page(from_path, template_path, dest_path)
    else:
      generate_pages_recursive(from_path, template_path, dest_path)

    # if os.path.isdir(concat_src_path):
    #   rec_file = os.listdir(concat_src_path)
    #   print("curent",concat_src_path)
    #   os.makedirs(os.path.join(dest_dir_path, file),exist_ok = True)
    #   src_path = os.path.join(dir_path_content, file)
    #   dest_path = os.path.join(dest_dir_path, file)
    #   generate_pages_recursive(src_path, template_path, dest_path)
    # else:
    #   if pathlib.Path(file).suffix == ".md":
    #     dest_file = file.rstrip("md")
    #     print("gen file", os.path.join(dir_path_content,file))
    #     generate_page(concat_src_path, template_path, os.path.join(dest_dir_path ,dest_file+"html"))

def generate_page(from_path, template_path, dest_path):
  print(f"Generating Page from {from_path} to {dest_path} using {template_path}")
  source_path = open(from_path, "r")
  markdown_content = source_path.read()
  source_path.close()

  template_file = open(template_path, "r")
  template = template_file.read()
  template_file.close

  node = markdown_to_html_node(markdown_content)
  html = node.to_html()

  page_title = extract_title(markdown_content)
  template = template.replace("{{ Title }}", page_title)
  template = template.replace("{{ Content }}", html)

  dest_dir_path = os.path.dirname(dest_path)
  if dest_dir_path != "":
    os.makedirs(dest_dir_path, exist_ok=True)
  to_file = open(dest_path, "w")
  to_file.write(template)

def extract_title(markdown):
  lines = markdown.split("\n")
  for line in lines:
    if line.startswith("# "):
      return line
  else:
    raise ValueError("Invalid Header")
