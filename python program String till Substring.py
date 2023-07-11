#python program String till Substring

str1 = input("Enter your string: ")

split = input("Enter your word to split from there: ")

print("Your Original string: ", str1)
print("Your Split string: ", split)

res = str1.partition(split)[0] 

print("String before the substring occurance: ",res)
