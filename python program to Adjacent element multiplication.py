# python program to Adjacent element multiplication
tuple1 = (1,4,5,6,7,10)

print("The orginal tuple is : ",  str(tuple1))
res = tuple(i * j for i ,j in zip(tuple1,tuple1[1:]))

print("tuple After multiplication : ", str(res))
