# python program to Skew Nested Tuple Summation

tuple1 = (10,(20,(30,(40,(6,None)))))

print("The Orginal tuple is: ", str(tuple1))
res = 0
while tuple1:
    res += tuple1[0]
    tuple1 = tuple1[1]

print("The Summation of first position: ", str(res))
