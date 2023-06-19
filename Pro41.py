# Python program to check if a string has at least one letter and one number

def check(str1):

    flagl = False
    flagd = False

    for i in str1:
        if i.isalpha():
            flagl = True
        if i.isdigit():
            flagd = True
    
    return flagl and flagd

str1 = input("Enter Your String: ")
print("Your string is true or false: ", check(str1))

