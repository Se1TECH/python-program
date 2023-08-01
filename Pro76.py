#python program to Elements Frequency in Mixed Nested Tuple


def flatten(Tuple1):
    for tup in Tuple1:
        if isinstance(tup, tuple):
            yield from flatten(tup)
        else:
            yield tup

tuple1 = (1,2,(1,4),5,6,7,8,(9,2),(3,4),(5,6,7))
res = {}
for ele in flatten(tuple1):
    if ele not in res:
        res[ele] = 0
    res[ele] += 1

print("The element frequency : ", str(res))

