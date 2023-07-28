# python program to Convert Nested
#  Tuple to Custom Key Dictionary

tuple1 = ((3,"hello",7),(6,"welcome to",8),
(1,"video",2))

print("The Original string is: ", str(tuple1))
res = [{'key': sub[0],'value':sub[1],'id':sub[2]}
    for sub in tuple1]

print("the Converted dictionary: ", str(res))