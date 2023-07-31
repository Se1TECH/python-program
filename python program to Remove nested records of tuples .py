# python program to Remove nested records of tuples 

tuple1 = (1,2,3,4,5,(6,7),(8,9,10),11)

print("The Original tuple: ", str(tuple1))
res = tuple()
for count,ele in enumerate(tuple1):
    if not isinstance(ele, tuple):
        res = res+(ele,) 

print("The elements after remove nested tuples:  ",str(res))
