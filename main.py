import sys
import os 
import shutil
import tkinter
from easygui import *

def move_file():
  src = enterbox("What is the source of the file you want to move?")
  dest = enterbox("Where do you want to move the file?\n")
  shutil.move(src, dest)
  print(f"file successfully moved to destionation folder")

def copy_file():
  src = enterbox("What is the source of the file you want to move?")
  dest = enterbox("Where do you want to move the file?\n")
  shutil.copyfile(src, dest)
  print(f"file successfully copied to destionation folder")

def delete_file():
  path = enterbox("Which file you want to delete")
  os.remove(path)

def rename_file():
  file_rename = enterbox("Which file you want to rename?")
  name_rename = enterbox("What you want to rename it to?")
  os.rename(file_rename, name_rename)
  print("file successfully renamed")

while 1:
  msg = "which file operation do you want to do?\n"
  title="File Manager"
  choices = ["Copy file", "Move file", "Delete file", "Rename file"]
  choice = choicebox(msg, title, choices)
  # msg = "Do you want to perform this action now?"
  if choice == 'Move file':
    pass
    move_file()
  elif choice == 'Copy file':
    pass
    copy_file()
  elif choice == 'Delete file':
    pass
    delete_file()  
  elif choice == 'Rename file':
    pass
    rename_file()
  else:
    sys.exit(0)

