# print the extension of file enter by users

fileName = input("Enter File Name with extension: ")
fileExt = fileName.split(".")
print("The Extension of file is: " , repr(fileExt[-1]))