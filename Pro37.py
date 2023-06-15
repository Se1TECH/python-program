# Python program to multiply all values in the
# list using traversal

def mul1(list1):
    mul = 1
    for x in list1:
        mul = mul * x
    return mul

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print("Mutiplication of ALL list Item: ", mul1(list1))
print("Mutiplication of ALL list Item: ", mul1(list2))
