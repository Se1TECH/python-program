#  python program to Sort lists in tuple

tuple1 = ([5,2,3,],[8,5,7],[5,4,2],[9,6,7])
print("The Orignal Tuple is: ",  str(tuple1))
res = tuple((sorted(sub) for sub in tuple1 ))
print("The Tuple after sorting lists: ", str(res))