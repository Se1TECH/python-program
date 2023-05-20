#File Handling in python

# Open File
file1 = open("file1.txt")

if file1:
    print("File Open Successfully")

# Close file
file1.close()

# Write into text file
file1 = open("file1.txt","w")

if file1:
    file1.write("This is my new added content vcchjchjjhxzvchj")
file1.close()


# Read from text file

file1 = open("file1.txt","r")

if file1:
    content = file1.read()
    print("Content of file is: " , content)

file1.close()
