#Python program from given list 
# having number and its cube in each tuple

list1 = []
n= int(input("Enter Numbers of element use need in list: "))

for i in range(0,n):
    ele = int(input())
    list1.append(ele)

print("Your list is : ", list1)
res = [(val,pow(val, 3)) for val in list1]

print("Your list with cube is : ", res)
