# python program to sort the list of tuples in alphabetically
def sort_tuple(tuple1):
    n= len(tuple1)
    for i in range(n):
        for j in range(n-i-1):
            if tuple1[j][0] > tuple1[j+1][0]:
                tuple1[j],tuple1[j+1] = tuple1[j+1],tuple1[j]

    return tuple1

tuple1 = [("Ajay",10),("Zenat",30),("John",60),("Rancho","C"),("Abhi",48)]

print("After Sorting tuple: ",sort_tuple(tuple1))


