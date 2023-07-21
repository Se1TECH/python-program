# python program to Flatten tuple of List to tuple

tuple1 = ([1,2],[6,7,18,6],[5])

print("The original tuple: ",str(tuple1))
res = tuple(sum(tuple1,[]))
print("The Flattend tuple: ", str(res))