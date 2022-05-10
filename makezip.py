import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
# Check if file exists
	if path.exists("/tmp/F5_details.txt"):
# get the path to the file in the current directory
	src = path.realpath("F5_details.txt");
# rename the original file
	os.rename("career.guru99.txt","guru99.txt")
# now put things into a ZIP archive
	root_dir,tail = path.split(src)
        shutil.make_archive("guru99 archive", "zip", root_dir)
# more fine-grained control over ZIP files
	with ZipFile("testguru99.zip","w") as newzip:
	newzip.write("F5_details.txt")
	    newzip.write("F5_details.txt.bak")
if __name__== "__main__":
	  main()
