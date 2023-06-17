# Remove the ith character from the string using the native method

str1 = input("Enter your string: ")
pos = int(input("Enter ith posistion to remove: "))

new_str = ""

 
for i in range(len(str1)):
    if i != pos-1:
      new_str = new_str + str1[i]

print("The String after remove ith position: ", new_str)  
