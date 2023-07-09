# python program to Test if string is subset of another
str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")

print("\n\nOriginal string 1: ", str1)

res = all(ele in str1 for ele in str2)

print("Does String contains another string or not: ", str(res))
