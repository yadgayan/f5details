from zipfile import ZipFile
import pyminizip
import os
from os.path import basename
# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
   # create a ZipFile object
   with ZipFile(zipFileName, 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
               if filter(filename):
                   # create complete filepath of file in directory
                   filePath = os.path.join(folderName, filename)
                   # Add file to zip
                   zipObj.write(filePath, basename(filePath))
def main():
    print('*** Create a zip file from multiple files  ')
    #create a ZipFile object
    zipObj = ZipFile('/tmp/sample.zip', 'w')
    
    # Add multiple files to the zip
    zipObj.write('/tmp/F5_details.txt')
    
    
    # close the Zip File
    zipObj.close()
    
     # input file path
    inpt = "'/tmp/F5_details.txt"
  
      # prefix path
    pre = None

      # output zip file path
    oupt = "/tmp/sample2.zip"

      # set password value
    password = "GFG"

      # compress level
    com_lvl = 5

      # compressing file
    pyminizip.compress(inpt, None, oupt,password, com_lvl)
 

if __name__ == '__main__':
   main()
