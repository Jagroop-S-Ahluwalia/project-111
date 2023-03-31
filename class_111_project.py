import os
import shutil

from_dir = r"C:\Users\jagsm\Downloads"
to_dir = r"C:\Users\jagsm\Downloads\document_file"

listoffiles = os.listdir(from_dir)

print(listoffiles)

for i in listoffiles:
    name, extention = os.path.splitext(i)
    print(name)
