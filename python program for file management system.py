# python program for file management system
import os

def create_file():
    file_name = input("Enter file name: ")
    content = input("Enter Your content of file: ")

    try:
        with open(file_name, "w") as file:
            file.write(content)
        print("File Created Successfully.")
    except:
        print("Error to creating file.")

def read_file():
    file_name = input("Enter File name to read: ")

    try:
        with open(file_name, "r") as file:
            content = file.read()
        print(f"File Content:\n {content}") 
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Error to reading file.")

def upadate_file():
    file_name = input("Enter file name to update: ")
    content = input("Enter the new content: ")

    try :
        with open(file_name,"w") as file:
            file.write(content)
        print("File Updated Successfully.")
    except FileNotFoundError:
        print("File Not Found.")
    except:
        print("Error to updating file.")

def delete_file():
    file_name = input("Enter the file name to delete: ")

    try:
        os.remove(file_name)
        print("File Deleted Successfully.")
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Error deleting file.")


#menu loop
while True:
    print("\n\n----- File Management System -----")
    print("1. Creating file")
    print("2. Read file")
    print("3. Update file")
    print("4. Delete file")
    print("5. Exit")

    choice = input("Enter your choice[1-5]: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        upadate_file()
    elif choice == "4":
        delete_file()
    elif choice == "5":
        print("Exiting the Program.")
        break
    else:
        print("Invalid Choice, Please Try again.")

