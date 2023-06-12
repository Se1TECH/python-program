# python code to Check if element exists in list or not

list1 = []

n = int(input("Enter Number of element you want in list: "))
print("Enter ", n," elements in list : ")
for i in range(0,n):
    element = int(input())
    list1.append(element)

ele = int(input("Which element you want to search in list: "))

if ele in list1:
    print(ele," is exist")
else:
    print(ele," does not exist")

