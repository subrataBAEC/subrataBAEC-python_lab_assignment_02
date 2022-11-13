## subrataBAEC-python_lab_assignment_02

### Event driven programming using python
-------------------------
### Instructions:
---------------
1. make sure the path is the server folder
2. Copy all or individual files to the source folder (this can be done before the code execution or during the execution)

### Code description:
-------------------
1. This code detects events in the source folder
2. Takes multiple files from the source and executes
3. If the file is a text file, it makes 3 copies to the server folder and then makes a zip file and sends it to the destination folder, and finally unzips.
4. If the file is a python file, it executes and captures output and errors.
5. If the file is neither text nor a python file, the file considers an invalid file type.
6. As the code continues to seek for new files in the source folder, to stop the code, apply keyboard interrupt.
