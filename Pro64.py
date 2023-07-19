# python program to Remove None Tuples from List

list1 = [(None,None),(None,None),(3,6),(122,56),(None,)]
print("The original list is : ", str(list1))

res = [sub for sub in list1 if not all(ele == None for ele in sub)]

print("Removed None tuples : ", str(res))