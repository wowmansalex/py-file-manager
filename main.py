import os 
import shutil

#get the source directory
src = input("What is the source of the file you want to move?\n")

#get the the target directory
dest = input("Where do you want to move the file?\n")
#function that moves file from source to target directory

def move_file(src,dest):
  shutil.move(src, dest)
  print(f"file successfully moved to destionation folder")

move_file(src, dest)
