# python program to sum of all items in a Dictionary

def returnSum(dict1):
    list1 = []
    for i in dict1:
        list1.append(dict1[i])
    final = sum(list1)

    return final

dict1 = {'a':10,'b':30,'c':886}
print("The Sum is : ", returnSum(dict1))
