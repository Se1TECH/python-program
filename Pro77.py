# python program to Unique elements in nested tuple
tuple_list = [(1,2,3),(3,4,5),(4,5,6),(3,4,6)]

print("\nThe Orginal list: ", str(tuple_list))

res = []
temp = set()
for inner in tuple_list:
    for ele in inner:
        if not ele in temp:
            temp.add(ele)
            res.append(ele)

print("Unique elements in nested tuples are : ", str(res))