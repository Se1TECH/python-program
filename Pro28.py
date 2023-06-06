# Write a program to print multiplication table of a given number
num = int(input("Enter number for print table: "))

for i in range(1,11):
    ans = num * i
    print(num, " * ", i, " = ", ans)