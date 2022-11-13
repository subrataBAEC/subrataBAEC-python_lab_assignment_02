# lab exam module 23
# cd .\server\
# go back: cd..
# use ctrl+c to stop infinte loop

""""
Event driven programming using python
-------------------------
Instructions:
---------------
1. make sure the path is the server folder
2. Copy all or individual files to the source folder (this can be done before the code execution or during the execution)

Code description:
-------------------
1. This code detects events in the source folder
2. Takes multiple files from the source and executes
3. If the file is a text file, it makes 3 copies to the server folder and then makes a zip file and sends it to the destination folder, and finally unzips.
4. If the file is a python file, it executes and captures output and errors.
5. If the file is neither text nor a python file, the file considers an invalid file type.
6. As the code continues to seek for new files in the source folder, to stop the code, apply keyboard interrupt.
"""

import glob
import shutil
import os
from zipfile import ZipFile
import time
import sys 

# function to truncate copies files in server folder
def truncate_text_files(file_name, item):
    f=open(file_name,"r")
    lst=[]
    i=0
    for x in f:
        i+=1
        # print(x)
        lst.append(x)
        # f.write(x)
        if i==(item)*10:
            break
    f.close()
    # print(lst)
    f=open(file_name,"w")
    for element in lst:
        f.write(element)
    f.close()


# folder paths
server_path="../server/"
source_path="../source/*"
destination_path="../destination"
nums=[1,2,3] # for 3 text files


try:
    while True:
        print("\n")
        time.sleep(5)
        # see files inside source folder-in a list
        source_object=glob.glob(source_path)
        # print(f"all source_objects(a list): {source_object}") # desired object
        if len(source_object)>0:
            # copy the some.txt file to server folder
            object_path=source_object[0]
            # print(f"desired object path(a str): {object_path}")

            # extract object name from object path string using split
            object_name=object_path.split("\\")[-1].split(".")
            # print(f"object name after spliting (list): {object_name}")
        
            if object_name[-1]=="py": # pytthon file
                print("this is a valid python file")
                # sys.stdout = open("log.txt", "a") # capturing all terminal outputs in log.txt, but terminal o/p does not work
                
                # capturing outputs and errors from .py files
                try:
                    exec(open(object_path).read())
                except:
                    error=sys.exc_info()[0]
                    print(f"{error} occured")                

            elif object_name[-1]=="txt": # text file
                print("this is a valid text file")

                # add postfix to some.txt and copy to destination folder
                prefix=object_name[0]
                postfix=object_name[1]
                all_file_names=[]

                for item in range(len(nums)):
                    # print(item)
                    item=item+1
                    file_name=prefix+ "_"+ str(item)+ "."+ postfix
                    # print(file_name)

                    #copy to server folder
                    shutil.copy(object_path,f"{server_path}/{file_name}")
                    truncate_text_files(file_name,item)
                    all_file_names.append(file_name)

                # text files in zip
                my_zip="new_file.zip"
                with ZipFile(my_zip,"w") as nz:
                    for item in all_file_names:
                        nz.write(item)

                # copy this zip to destination and remove from server
                shutil.copy(my_zip,destination_path)
                os.remove(my_zip) 

                # open archhive file in destination
                shutil.unpack_archive("../destination/new_file.zip", f"{destination_path}/new_file")
            else:
                print("file is not valid python or text file")
                
            # time.sleep(10)
            os.remove(object_path) # delete source file
            # sys.stdout.close()
    
except: 
    print("stopped by the user: keyboard interrupt")
    # sys.stdout.close()
    # fileObject = open("log.txt", "r")
    # data = fileObject.read()
    # print(data)