# Python Right and Left Shift characters in String

str1 = input("Enter Your String: ")
left = int(input("Enter left shift:  "))
right = int(input("Enter right shift:  "))

print("The original string : ", str1)

res =  (str1 * 3)[len(str1) + right-left: 2* len(str1) + right -left]

print("String After rotation: ", str(res))
