#python program to Extract Symmetric Tuples

tuple1 = [(1,2),(3,4),(5,6),(7,8),(4,3),(6,5)]
print("The orginal tuple list :  ", str(tuple1))
temp = set(tuple1) & {(b,a) for a,b in tuple1}
res = {(a,b) for a,b in temp if a<b}
print("Symetric tuples: ", str(res))