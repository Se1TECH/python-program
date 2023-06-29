#python program to Convert Snake case to Pascal case
str1 = input("Enter snake String: ")

print("\nOrginal string: ", str1)

res = str1.replace("_", " ").title().replace(" ", "")

print("\nThe String after changing case: ", str(res))
