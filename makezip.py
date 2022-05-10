from zipfile import ZipFile
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
    zipObj.write('F5_details.txt')
    
    # close the Zip File
    zipObj.close()
 
   
 
if __name__ == '__main__':
   main()
