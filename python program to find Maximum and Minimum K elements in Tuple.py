# python program to find Maximum and Minimum K elements in Tuple

tuple1 = (2,13,4,5,6,10,20)

print("Original tuple list is : ", str(tuple1))
k=1
res = []
tuple1 = list(sorted(tuple1))

for idx,val in enumerate(tuple1):
    if idx <k or idx >=  len(tuple1)-k:
        res.append(val)
res = tuple(res) 
print("The Extracted values : ", str(res))
