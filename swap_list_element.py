# Find the length of the list and simply swap 
# the first element with last element.

def listSwap(list1):
    size = len(list1)
    temp = list1[0]
    list1[0] = list1[size-1]
    list1[size-1] = temp
    return list1

list1 = [180,20,30,40,50,600]
print("After Swap first and last list element : ", listSwap(list1))
