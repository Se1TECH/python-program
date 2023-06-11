# Python3 program to swap elements
# at given positions

def swapPos(list1,pos1,pos2):
    list1[pos1],list1[pos2] = list1[pos2],list1[pos1]
    return list1

list1 = [] 
n = int(input("Enter Number of Element you want in list: "))
for i in range(0,n):
    element = int(input())
    list1.append(element)

pos1 = int(input("Enter 1st position to swap : "))
pos2 = int(input("Enter 2nd position to swap : "))

print("After Changing position in list: ", swapPos(list1,pos1-1,pos2-1))
