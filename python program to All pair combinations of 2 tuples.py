# python program to All pair combinations of 2 tuples
tuple1 = (3,6)
tuple2 = (4,7)

print("First original tuple: ", tuple1)
print("Second original tuple: ", tuple2)

res = [(a,b) for a in tuple1 for b in tuple2]
res = res + [(a,b) for a in tuple2 for b in tuple1]

print("The Filtered Tuple: ",  str(res))
