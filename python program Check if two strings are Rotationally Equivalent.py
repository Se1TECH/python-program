# python program Check if two strings are Rotationally Equivalent
str1 = input("Enter Your String 1 : ")
str2 = input("Enter Your String 2 : ")

print("\n\nOriginal string 1: " , str1)
print("Original string 2: " , str2)

res = False
for idx in range(len(str1)):
    if str1[idx: ] + str1[ :idx] == str2:
        res = True
        break

print("\n\nAre two String Rotationally Equivalent: ", str(res))
