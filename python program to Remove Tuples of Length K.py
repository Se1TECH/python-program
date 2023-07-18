# python program to Remove Tuples of Length K

list1 = [(4,3),(4, ),(8,4,5),(5, ),(8,3,7,9),(2, )]
print("The Original list is: ", str(list1))
k=1

res = [ele for ele in list1 if len(ele) != k]

print("Filtered list : ", str(res))
